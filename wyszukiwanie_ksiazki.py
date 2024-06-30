import json


def wyszukaj_ksiazke(tytul,autor,isbn,id_ksiazki):
    with open('ksiazki.json','r') as f:
        ksiazki = json.load(f)
        

    results = [ksiazka for ksiazka in ksiazki if ksiazka['tytul'] == tytul and ksiazka['autor'] == autor and ksiazka['isbn'] == isbn and ksiazka['id_ksiazki'] == id_ksiazki]
    return results

