import json

def wypozyczanie_ksiazek(uzytkownik_id, ksiazka_id, data_wypozyczenia, data_zwrotu):
    with open('wypozyczenia.json', 'r') as f:
        wypozyczenia = json.load(f)

        nowe_wypozyczenie = {
            "id": len(wypozyczenia) + 1,
            "uzytkownik_id": uzytkownik_id,
            "ksiazka_id": ksiazka_id,
            "data_wypozyczenia": data_wypozyczenia,
            "data_zwrotu": data_zwrotu
        }

        wypozyczenia.append(nowe_wypozyczenie)

        with open('wypozyczenia.json', 'w') as f:
            json.dump(wypozyczenia, f, indent=4)

        with open('ksiazki.json', 'r') as f:
            ksiazki = json.load(f)

            for ksiazka in ksiazki:
                if ksiazka['id'] == ksiazka_id:
                    ksiazka['wypozyczone'] = True
                    break

            with open('ksiazki.json', 'w') as f:
                json.dump(ksiazki, f, indent=4)
                
    print("Książka została wypozyczona.")



