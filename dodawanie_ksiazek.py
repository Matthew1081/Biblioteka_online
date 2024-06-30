import json

def dodawanie_ksiazek(tytul, autor, isbn):
    with open('ksiazki.json', 'r') as f:
        ksiazki = json.load(f)

        nowa_ksiazka = {
        "id": len(ksiazki) + 1,
        "tytul": tytul,
        "autor": autor,
        "isbn": isbn
        }

        ksiazki.append(nowa_ksiazka)

        with open('ksiazki.json', 'w') as f:
            json.dump(ksiazki, f, indent=4)

        print("Książka została dodana.")

#def usuwanie_ksiazek(id, tytul, autor, isbn):
#    with open('ksiazki.json', 'r') as f:
#        ksiazki = json.load(f)

 #   usun_ksiazke
        