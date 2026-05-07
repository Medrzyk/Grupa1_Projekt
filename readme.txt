===PROJEKT - ETAP 3===
Numer grupy: 1
Nazwa projektu: Analiza sentymentu i trendów sprzedażowych Amazon (LLM Integration)
Opis: Projekt skupia się na analizie danych ustrukturyzowanych z Amazon Sales Dataset. W trzecim etapie zintegrowano model LLM do automatycznej analizy wydźwięku (sentiment analysis) recenzji klientów.

===GRUPA===
Lab grupa, ID, Nazwisko, Imie
2, 71642, Oleszczyński, Karol
2, 72559, Mędrzycki, Jakub
2, 72687, Ościłowski, Mariusz

===WKLAD - ETAP 3===
72559, Mędrzycki, Jakub: Implementacja potoku Transformers (sentiment-analysis), dobór modelu DistilBERT, przetwarzanie danych Amazon.csv.
71642, Oleszczyński, Karol: Opracowanie merytorycznej struktury raportu PDF i uzasadnienia wyboru modelu. Współautor dokumentacji README (część opisowa) oraz koordynacja spójności etapów projektu.
72687, Ościłowski, Mariusz: Analiza merytoryczna wyników modelu, interpretacja wygenerowanych wykresów oraz końcowa korekta raportu pod kątem wymagań technicznych.


===PYTANIA BADAWCZE===
1. Jaki jest wpływ wysokości rabatów na oceny produktów wystawiane przez klientów?
2. Które kategorie produktów na Amazonie generują największe zaangażowanie (liczbę opinii)?
3. Czy stopień zadowolenia klienta (ocena) koreluje z długością wystawianej recenzji?
4. (Etap 3) W jakim stopniu model LLM (DistilBERT) poprawnie interpretuje wydźwięk recenzji w porównaniu do ocen numerycznych?

===ZRODLA DANYCH===
Nazwa danych: Amazon Sales Dataset
Dataset URL: https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset

===ZMIENNE KLUCZOWE===
product_name, category, rating, rating_count, discount_percentage, review_content

===CECHY WYPROWADZONE===
main_category, review_length, ai_sentiment (predykcja modelu)

===MODEL LLM (ETAP 3)===
Nazwa: distilbert-base-uncased-finetuned-sst-2-english
Typ: Text Classification (Sentiment Analysis)
Zastosowanie: Automatyczna klasyfikacja treści recenzji na pozytywne i negatywne.

===SRODOWISKO===
Python version: 3.13.13
Biblioteki: pandas==3.0.2, matplotlib==3.10.8, transformers==4.44.2, torch==2.4.0

===ZAWARTOSC REPOZYTORIUM===
Grupa1_Projekt/
|--- Data/
|   |--- amazon.csv
|--- outputs/
|   |--- Wykres1.png 
|   |--- Wykres2.png 
|   |--- Wykres3.png 
|--- main.py 
|--- requirements.txt
|--- raport.pdf 
