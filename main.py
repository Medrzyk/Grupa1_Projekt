import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from transformers import pipeline
from datasets import Dataset
from transformers import AutoTokenizer
import evaluate
from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer

df = pd.read_csv("Data/amazon.csv")

#Eksploracja danych

#print(df)
#print(df.isnull().sum())
#print(df.columns)
#print(df["discount_percentage"].head(15)) 
#print(df.loc[df["rating_count"].isnull(), "rating_count"])
# df = df.dropna(subset=["rating_count"]) # Usuniecie pustych wierszy
#print(df.isnull().sum())
# print(df.describe())
# print(df["rating"].unique())
# print(df["category"].unique())
# print(df.groupby("rating")["rating"].count())
# print(df["product_name"].unique())
# print(df["category"].value_counts().head(5))
# print(df["discount_percentage"].unique())
df = df[df["rating"] != "|"]
# print(df.loc[df["rating"] == "|", ["product_name", "rating", "discount_percentage"]])
df["rating"] = df["rating"].astype(float)
df["discount_percentage"] = df["discount_percentage"].str.replace("%", "").astype(float)

# 1 pytanie badawcze (Jaki jest wplyw rabatow na zadowolenie klientow)
plt.figure(figsize=(10, 6))
plt.scatter(df["discount_percentage"], df["rating"], alpha=0.5, color="teal")
plt.title("Wplyw wysokosci rabatu na ocene produktu")
plt.xlabel("Znizka (%)")
plt.ylabel("Ocena (1-5)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("outputs/Wykres1.png")
plt.show()

#2 pytanie badawcze (Jakie kategorie generuja nawiecej opini?)
df["rating_count"] = df["rating_count"].str.replace(",", "").astype(float)
df["main_category"] = df["category"].str.split("|").str[0]
popularnosc = df.groupby("main_category")["rating_count"].sum().sort_values(ascending=False).head(5)

plt.figure(figsize=(10, 6))
popularnosc.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("5 najpopularniejszych kategorii na Amazonie wedlug ilosci ocen")
plt.xlabel("Glowna kategoria")
plt.ylabel("Laczna liczba opinii (w milionach)")
plt.tight_layout()
plt.savefig("outputs/Wykres2.png")
plt.show()

#3 pytanie badawcze (Czy ocena wplywa na dlugosc opini?)
df["review_length"] = df["review_content"].astype(str).str.len()
df["rating_rounded"] = df["rating"].round()
dlugosc_opinii = df.groupby("rating_rounded")["review_length"].mean()
plt.figure(figsize=(10, 6))
dlugosc_opinii.plot(kind="bar", color="mediumpurple", edgecolor="black")
plt.title("Srednia dlugosc recenzji a ocena produktu")
plt.xlabel("Ocena produktu (zaokraglona)")
plt.ylabel("Srednia liczba znakow w recenzji")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/Wykres3.png")
plt.show()


#Etap 3 model transformers Distilbert 

df_sample = df.sample(n=50, random_state=42).copy()
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
def get_sentiment(text):
    text = str(text)[:512]
    result = sentiment_pipeline(text)[0]
    return result["label"]
df_sample["ai_sentiment"] = df_sample["review_content"].apply(get_sentiment)
df_sample["rating_category"] = df_sample["rating"].apply(lambda x: "POSITIVE" if x >= 4 else ("NEGATIVE" if x <= 3 else "NEUTRAL"))
zgodnosc = (df_sample["ai_sentiment"] == df_sample["rating_category"]).mean() * 100
print(df_sample[["rating", "rating_category", "ai_sentiment", "review_content"]].head(10))
print(f"Zgodnosc modelu AI z ocenami klientow: {zgodnosc}%")

# Etap 4 

df_clean = df.dropna(subset=["review_content", "rating"]).copy()
df_clean["label"] = df_clean["rating"].apply(lambda x: 1 if x >= 4 else 0)

df_train = df_clean.sample(n=200, random_state=42)
df_eval = df_clean.sample(n=20, random_state=24)

dataset_train = Dataset.from_pandas(df_train[["review_content", "label"]])
dataset_eval = Dataset.from_pandas(df_eval[["review_content", "label"]])

tokenizator = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

def tokenizuj_tekst(przyklady):
    return tokenizator(przyklady["review_content"], truncation=True, padding="max_length", max_length=128)

dataset_train = dataset_train.map(tokenizuj_tekst, batched=True)
dataset_eval = dataset_eval.map(tokenizuj_tekst, batched=True)

model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english", num_labels=2)

argumenty_treningu = TrainingArguments(
    output_dir="outputs/wyniki_tuning",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=2,
    weight_decay=0.01,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    report_to="none"
)

metryka = evaluate.load("accuracy")

def oblicz_metryki(wyniki_predykcji):
    logity, etykiety = wyniki_predykcji
    predykcje = np.argmax(logity, axis=1)
    return metryka.compute(predictions=predykcje, references=etykiety)

trener = Trainer(
    model=model,
    args=argumenty_treningu,
    train_dataset=dataset_train,
    eval_dataset=dataset_eval,
    compute_metrics=oblicz_metryki,
)
trener.train()

ocena_koncowa = trener.evaluate()
print(f"Dokladnosc modelu po fine-tuningu: {ocena_koncowa["eval_accuracy"] * 100}%")