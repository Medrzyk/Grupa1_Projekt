===PROJEKT===
Numer grupy: 1
Nazwa projektu: Analiza zachowań zakupowych klientów (Customer Purchase Behavior)
Opis: Celem projektu jest analiza ustrukturyzowanych danych sprzedażowych w celu zidentyfikowania czynników wpływających na wysokość wydatków klientów oraz popularność produktów w zależności od sezonu.

===GRUPA===
Lab grupa, ID, Nazwisko, Imie
2, 71642, Oleszczyński, Karol
2, 72559, Mędrzycki, Jakub
2, 72687, Ościłowski , Mariusz

===WKLAD===
ID, Nazwisko, Imie: Krótki opis wkładu każdego studenta do grupowego projektu na tym etapie.
72559, Medrzycki, Jakub: Stworzenie repozytorium na GitHub, napisanie kodu głównego (main.py), przeprowadzenie wstępnej analizy danych i sformułowanie pytań badawczych.
71642, Oleszczyński, Karol: Przygotowanie dokumentacji technicznej, opracowanie pliku README oraz struktury raportu końcowego dla Etapu 2.
72687, Ościłowski Mariusz: Analiza merytoryczna wyników, interpretacja wykresów oraz końcowa redakcja raportu PDF.

===PYTANIA BADAWCZE===
1. Czy rodzaj dostawy wpływa na kwotę zakupu?
2. Jak sezony wpływają na popularność produktów?
3. Która kategoria produktów generuje największe przychody?

===ZRODLA DANYCH===
Nazwa zrodla: Kaggle
Nazwa danych: Customer Purchase Behavior Analysis
Dataset URL: https://www.kaggle.com/datasets/arfeenkabir/customer-purchase-behavior-analysis

===ZMIENNE===
Customer ID, Age, Gender, Item Purchased, Category, Purchase Amount (USD), Location, Size, Color, Season, Review Rating, Subscription Status, Payment Method, Shipping Type, Discount Applied, Promo Code Used, Previous Purchases, Preferred Payment Method, Frequency of Purchases

===CECHY===
Average_Purchase_Amount_Per_Category, Popular_Product_By_Season, Shipping_Type_Mean_Spend

===ANALIZA===
1. Analiza średniej kwoty zakupu w zależności od wybranego rodzaju dostawy (wykres słupkowy).
2. Segmentacja 5 najpopularniejszych produktów dla każdego z czterech sezonów.
3. Porównanie średnich przychodów generowanych przez główne kategorie produktów.

===SRODOWISKO===
Python version: 3.13.13
Main libraries: pandas==3.0.2, matplotlib==3.10.8

===ZAWARTOSC===
P2_01_AnalizaZakupow/
|--- README.txt
|--- main.py
|--- raport.pdf
|--- requirements.txt
|--- Data/
|   |--- shopping_trends.csv
|--- outputs/
    |--- Wykres1.png
    |--- Wykres2.png
    |--- Wykres3.png