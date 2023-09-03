"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: David Barukčić
email: d.barukcic@seznam.cz
discord: David Barukčić
"""

import sys
import csv
import requests
from bs4 import BeautifulSoup

def main():
    # Kontrola, zda byly zadány správné argumenty příkazové řádky
    if len(sys.argv) != 3:
        print("Zadejte dva argumenty: <odkaz> <jmeno souboru.csv>.")
        return
    
    # Načtení argumentů z příkazové řádky
    odkaz = sys.argv[1]
    jmeno_souboru = sys.argv[2]
    
    try:
        # Získání dat z webu
        print("Data se zpracovávají...")
        data = stahnout_data(odkaz)
        if data:
            # Uložení dat do CSV souboru
            ulozit_data_do_csv(data, jmeno_souboru)
            print(f"Data byla uložena do souboru: {jmeno_souboru}")
        else:
            print("Nastala chyba při získávání dat.")
    except Exception as e:
        print(f"Nastala chyba: {e}")

def ulozit_data_do_csv(data, jmeno_souboru):
    zahlavi = data[0].keys()
    with open(jmeno_souboru, mode="w", encoding="utf-8", newline="") as csv_soubor:
        writer = csv.DictWriter(csv_soubor, fieldnames=zahlavi)
        writer.writeheader()
        writer.writerows(data)

def stahnout_data(odkaz):
    # Stáhne HTML obsah zadaného odkazu
    response = requests.get(odkaz)
    soup = BeautifulSoup(response.content, "html.parser")
    
    data_seznam = []
    for tabulka in soup.find_all("table", class_="table"):
        for obec in tabulka.find_all("tr")[2:]:
            kod_obce_element = obec.find("td", class_="cislo")
            nazev_obce_element = obec.find("td", class_="overflow_name")
            odkaz_obce = obec.find("a")
            
            if kod_obce_element and nazev_obce_element and odkaz_obce:
                kod_obce = kod_obce_element.text
                nazev_obce = nazev_obce_element.text
                odkaz_na_data = "https://volby.cz/pls/ps2017nss/" + odkaz_obce["href"]

                data_z_odkazu = ziskat_data(odkaz_na_data)
                hlasy = ziskat_hlasy(odkaz_na_data) 

                data_seznam.append({
                    "kód obce": kod_obce,
                    "název obce": nazev_obce,
                    **data_z_odkazu,
                    **hlasy
                })
        
    return data_seznam

def ziskat_data(data_odkaz):
    # Získá počet voličů, vydané obálky a platné hlasy z odkazu na detail obce
    response = requests.get(data_odkaz)
    data_soup = BeautifulSoup(response.content, "html.parser")
    
    volici = data_soup.find("td", headers="sa2").text
    vydane_obalky = data_soup.find("td", headers="sa3").text
    platne_hlasy = data_soup.find("td", headers="sa6").text
            
    return {
        "voliči v seznamu": volici,
        "vydané obálky": vydane_obalky,
        "platné hlasy": platne_hlasy,    
    }

def ziskat_hlasy(data_odkaz):
    # Získá počty hlasů pro jednotlivé strany z odkazu na detail obce
    response = requests.get(data_odkaz)
    data_soup = BeautifulSoup(response.content, "html.parser")

    hlasy_stran = {}
    for s in data_soup.find_all("td", headers=["t1sa1 t1sb2", "t2sa1 t2sb2"]):
        nazev_strany = s.text.strip()
        pocet_hlasu = s.find_next("td").text.strip()
        hlasy_stran[nazev_strany] = pocet_hlasu

    return hlasy_stran

if __name__ == "__main__":
    main()