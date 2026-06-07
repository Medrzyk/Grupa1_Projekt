===PROJEKT - ETAP 4 (FINAŁ)===
Numer grupy: 1
Nazwa projektu: Analiza sentymentu i trendów sprzedażowych Amazon (LLM Fine-Tuning)
Opis: Projekt skupia się na analizie danych tekstowych z Amazon Sales Dataset. W etapie finałowym przeprowadzono proces dostrajania (fine-tuning) modelu DistilBERT na specyficznych recenzjach konsumenckich w celu poprawy skuteczności klasyfikacji nastroju.

===GRUPA===
Lab grupa, ID, Nazwisko, Imie
2, 71642, Oleszczyński, Karol
2, 72559, Mędrzycki, Jakub
2, 72687, Ościłowski, Mariusz

===WKLAD - ETAP 4===
72559, Mędrzycki, Jakub: Przygotowanie skryptu fine-tuningu w Pythonie, przeprowadzenie tokenizacji danych za pomocą AutoTokenizer oraz optymalizacja hiperparametrów uczenia pod ograniczenia sprzętowe CPU.
71642, Oleszczyński, Karol: Opracowanie merytorycznej struktury finalnego raportu PDF, przygotowanie sekcji dotyczącej reprodukcji wyników oraz współautorstwo technicznej dokumentacji projektu.
72687, Ościłowski, Mariusz: Ewaluacja końcowa dokładności modelu po procesie dostrajania, opracowanie wniosków analitycznych oraz przygotowanie i aktualizacja instrukcji uruchomienia w pliku README.

===PYTANIA BADAWCZE===
1. Jaki jest wpływ wysokości rabatów na oceny produktów wystawiane przez klientów? (Brak bezpośredniej korelacji).
2. Które kategorie produktów na Amazonie generują największe zaangażowanie? (Dominacja kategorii Electronics).
3. Czy stopień zadowolenia klienta koreluje z długością recenzji? (Zadowoleni klienci piszą znacznie dłuższe opinie).
4. (Etap 4) O ile punktów procentowych wzrośnie dokładność modelu DistilBERT po dostrojeniu do e-commercowej domeny Amazona?

===ZRODLA DANYCH===
Nazwa danych: Amazon Sales Dataset (Kaggle)
Dataset URL: https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset

===MODEL LLM===
Bazowy model: distilbert-base-uncased-finetuned-sst-2-english
Dostrojony model zapisywany lokalnie w: outputs/wyniki_tuning/

===SRODOWISKO I BIBLIOTEKI===
Python version: 3.13.13
Wymagane pakiety: pandas==3.0.2, matplotlib==3.10.8, transformers==4.44.2, torch==2.4.0, datasets, evaluate

===INSTRUKCJA URUCHOMIENIA KODU I REPRODUKCJI WYNIKÓW===
Aby pomyślnie uruchomić projekt i odtworzyć proces treningu oraz analizy, wykonaj poniższe kroki:

1. Sklonuj lub pobierz repozytorium na swój dysk lokalny.
2. Upewnij się, że posiadasz zainstalowaną wersję Python 3.13.13.
3. Zainstaluj wymagane zależności za pomocą terminala:
   pip install -r requirements.txt
4. Uruchom główny skrypt programu:
   python main.py
5. Działanie programu:
   - Skrypt w pierwszej kolejności załaduje dane i wygeneruje wykresy statystyczne w folderze 'outputs/'.
   - Następnie wykona test bazowy potoku analizy sentymentu (Etap 3).
   - W ostatnim kroku rozpocznie się proces fine-tuningu na procesorze (CPU). Skrypt automatycznie utworzy lokalny folder 'outputs/wyniki_tuning/', gdzie zostaną zapisane wagi dostrojonego modelu, a w konsoli zostanie wyświetlona końcowa dokładność (Accuracy).

===ZAWARTOSC REPOZYTORIUM===
Grupa1_Projekt/
|--- Data/
|   |--- amazon.csv
|--- outputs/
|   |--- Wykres1.png (Korelacja rabat/ocena)
|   |--- Wykres2.png (Popularność kategorii)
|   |--- Wykres3.png (Asymetria długości opinii)
|   |--- wyniki_tuning/ (Generowany lokalnie po uruchomieniu main.py - wagi modelu)
|--- main.py (Pełny kod: EDA + Pipeline + Fine-tuning)
|--- requirements.txt
|--- raport.pdf (Raport końcowy Etapu 4)
|--- readme.txt
