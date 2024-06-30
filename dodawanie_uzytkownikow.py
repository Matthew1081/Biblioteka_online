import json

def dodawanie_uzytkownikow(imie,email):
    with open("uzytkownicy.json","r") as f:
        uzytkownicy = json.load(f)

        nowy_uzytkownik = {
            "id": len(uzytkownicy) + 1,
            "imie": imie,
            "email": email
        }
        uzytkownicy.append(nowy_uzytkownik)

        with open(uzytkownicy,"w") as f:
            json.dump(uzytkownicy,f,indent=4)
    