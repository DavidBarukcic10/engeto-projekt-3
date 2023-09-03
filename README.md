# Engeto-projekt-3: Elections scraper
Elections scraper
Popis projektu:
Tento skript je nástroj pro získání a ukládání dat o výsledcích voleb 2017 z vybraného územního celku na webu [Volby.cz](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ). Skript získává informace o čísle obce, názvu obce, počtu voličů, počtu vydaných obálek, počtu platných hlasů a výsledcích jednotlivých stran včetně počtu hlasů pro každou stranu.

# Instalace knihoven:
V kódu jsou použity knihovny requests pro stahování webových stránek a knihovny BeautifulSoup pro parsování HTML obsahu. Tyto knihovny lze nainstalovat ze souboru requirements.txt pomocí následujících příkazů:

> pip3 --version #overeni verze manazeru
> pip3 install requests #instalace knihovny requests
> pip install beautifulsoup4 #instalace knihovny beautifulsoup4

# Spuštění programu:
Spustíte skript main.py a v příkazovém řádku zadáte dva povinné argumenty.

odkaz: webová adresa, kde jsou dostupná volební data
jmeno souboru.csv: název výstupního CSV souboru, do něhož budou data uložena

# Příklad spuštění:
argument_1: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102
argument_2: Výsledky voleb Beroun.csv
Vzorový příklad: python main.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102" Výsledky voleb Beroun.csv

# Průběh stahování:
Zadejte dva argumenty: <odkaz> <jmeno souboru.csv>
Data se zpracovávají...
Data byla uložena do souboru: Výsledky_voleb_Beroun.csv

# Částečný výstup:
kód obce,název obce,voliči v seznamu,vydané obálky,platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie...
534421,Bavoryně,239,151,150,18,0,0,6,0,8,7,5,2,4,0,0,16,0,0,11,55,0,2,3,0,0,0,2,11,0
531057,Beroun,14 804,9 145,9 076,1 363,16,11,576,1,433,651,140,78,205,8,12,1 290,4,6,641,2 433,3,13,279,2,61,17,12,800,21
531073,Běštín,262,158,157,27,2,0,21,0,2,11,3,3,3,1,0,12,0,0,2,40,0,0,2,0,1,0,1,26,0
531081,Broumy,743,491,489,62,1,0,35,2,20,54,6,5,8,0,0,76,1,3,22,144,0,4,11,0,3,0,0,32,0

# Kontakt:
Autor: David Barukčić
E-mail: d.barukcic@seznam.cz
Discord: David Barukcic
