import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Data/shopping_trends.csv")

#Eksploracja danych
# print(df.head()) #Wyswietla 5 pierwszych wierszy z tabeli
# print(df.columns) #Wyswietla wszystkie nazwy kolumn
# print(df.shape) #Wielkosc tabeli danych
# print(df.isnull().sum()) #Sprawdzamy czy znajduja sie puste wiersze, jezeli tak to ile
# print(df.describe()) #Opis zebranych danych
# print(df["Shipping Type"].unique())
# print(df.groupby("Season")["Season"].count())
# print(df["Item Purchased"].unique())
# print(df.groupby("Season")["Item Purchased"].value_counts().head(5))
# print(df.groupby("Discount Applied")["Purchase Amount (USD)"].mean())
# print(df["Subscription Status"].unique())
# print(df.groupby("Subscription Status")["Purchase Amount (USD)"].mean()) 
# print(df["Category"].unique())
# print(df.groupby("Category")["Purchase Amount (USD)"].mean())

dane = df.groupby("Shipping Type")["Purchase Amount (USD)"].mean()
print(dane)

#Wykres 1 (Czy rodzaj dostawy wpływa na kwotę zakupu?)
dane.plot(kind="bar")
plt.title("Srednia kwota zakupu wzgledem rodzaju dostawy")
plt.xlabel("Rodzaj dostawy")
plt.ylabel("Srednia kwota (USD)")
plt.tight_layout()
plt.savefig("outputs/Wykres1.png")
plt.show()

# Wykres 2 Jak sezony wplywaja na popularność produktów?
dane2 = df.groupby("Season")["Item Purchased"].value_counts().groupby(level=0).head(5)
dane2.unstack(level=0).plot(kind="bar", figsize=(15,6),color=["orange", "green", "red", "blue"])
plt.title("Top 5 produktow w kazdym sezonie")
plt.xlabel("Produkt")
plt.ylabel("Liczba zakupow")
plt.tight_layout()
plt.savefig("outputs/Wykres2.png")
plt.show()

#Wykres 3 Która kategoria produktów generuje największe przychody?
dane3 = (df.groupby("Category")["Purchase Amount (USD)"].mean())
dane3.plot(kind="bar")
plt.title("Która kategoria produktów generuje największe przychody?")
plt.xlabel("Kategoria")
plt.ylim(55,62)
plt.ylabel("Srednia kwota zakupu")
plt.tight_layout()
plt.savefig("outputs/Wykres3.png")
plt.show()
