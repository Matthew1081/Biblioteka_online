from flask import Flask, render_template, request, jsonify
import json

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dodawanie_ksiazek', methods=['GET', 'POST'])
def dodawanie_ksiazki():
    if request.method == 'POST':
        tytul = request.form['tytul']
        autor = request.form['autor']
        isbn = request.form['isbn']
        dodaj_ksiazke_do_bazy(tytul, autor, isbn)
        return render_template('dodawanie_ksiazek.html')

def dodaj_ksiazke_do_bazy(tytul, autor, isbn):
    with open('ksiazki.json', 'r') as f:
        ksiazki = json.load(f)

        nowa_ksiazka = {
            'id': len(ksiazki) + 1,
            'tytul': tytul,
            'autor': autor,
            'isbn': isbn,
            "dostepnosc": True
        }

        ksiazki.append(nowa_ksiazka)

        with open('ksiazki.json', 'w') as f:
            json.dump(ksiazki, f, indent=4)

@app.route('/dodawanie_uzytkownikow', methods=['GET', 'POST'])
def dodawanie_uzytkownikow():
    if request.method == 'POST':
        imie = request.form['imie']
        email = request.form['email']
        dodaj_uztkownika_do_bazy(imie, email)
        return render_template('dodawanie_uzytkownikow.html')


def dodaj_uztkownika_do_bazy(imie, email):
    with open('uzytkownicy.json', 'r') as f:
        uzytkownicy = json.load(f)

        nowy_uzytkownik = {
            'id': len(uzytkownicy) + 1,
            'imie': imie,
            'email': email,
        }

        uzytkownicy.append(nowy_uzytkownik)

        with open('uzytkownicy.json', 'w') as f:
            json.dump(uzytkownicy, f, indent=4)


def load_books():
    with open('ksiazki.json', 'r') as file:
        books = json.load(file)
    return books


def search_books(title):
    books = load_books()
    results = [book for book in books if title.lower() in book['tytul'].lower()]
    return results

@app.route('/wyniki_wyszukiwania_ksiazek', methods=['GET'])
def wyniki_wyszukiwania_ksiazek():
    tytul = request.args.get('tytul', '')
    wyniki = search_books(tytul)
    return render_template('wyniki_wyszukiwania_ksiazek.html', wyniki=wyniki)
         

if __name__ == '__main__':
    app.run(debug=True)
            