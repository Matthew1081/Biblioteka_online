from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import json
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'supersecretkey'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_register'

class User(UserMixin):
    def __init__(self, id, username, password, role, email):
        self.id = id
        self.username = username
        self.password = password
        self.role = role
        self.email = email

    def get_id(self):
        return self.id

@login_manager.user_loader
def load_user(user_id):
    with open('uzytkownicy.json', 'r') as file:
        users = json.load(file)
    for user in users:
        if user['id'] == int(user_id):
            return User(user['id'], user['username'], user['password'], user['role'], user['email'])
    return None

@app.route('/login_register', methods=['GET', 'POST'])
def login_register():
    if request.method == 'POST':
        if 'login' in request.form:
            username = request.form['username']
            password = request.form['password']
            with open('uzytkownicy.json', 'r') as file:
                users = json.load(file)
            for user in users:
                if user['username'] == username and user['password'] == password:
                    login_user(User(user['id'], user['username'], user['password'], user['role'], user['email']))
                    flash('Successfully logged in!', 'success')
                    return redirect(url_for('index'))
            flash('Invalid credentials!', 'danger')
        elif 'register' in request.form:
            username = request.form['reg_username']
            password = request.form['reg_password']
            email = request.form['reg_email']
            role = request.form['role']
            with open('uzytkownicy.json', 'r') as file:
                users = json.load(file)
            new_user = {
                "id": len(users) + 1,
                "username": username,
                "password": password,
                "email": email,
                "role": role
            }
            users.append(new_user)
            with open('uzytkownicy.json', 'w') as file:
                json.dump(users, file, indent=4)
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login_register'))
    return render_template('login_register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successfully logged out!', 'success')
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dodawanie_ksiazek', methods=['GET', 'POST'])
@login_required
def dodawanie_ksiazek():
    if request.method == 'POST':
        tytul = request.form['tytul']
        autor = request.form['autor']
        isbn = request.form['isbn']
        dodaj_ksiazke_do_bazy(tytul, autor, isbn)
        flash('Book added successfully!', 'success')
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
@login_required
def dodawanie_uzytkownikow():
    if request.method == 'POST':
        imie = request.form['username']
        email = request.form['email']
        password = request.form["password"]
        dodaj_uzytkownika_do_bazy(imie, email, password)
        flash('User added successfully!', 'success')
    return render_template('dodawanie_uzytkownikow.html')

def dodaj_uzytkownika_do_bazy(imie, email, password):
    with open('uzytkownicy.json', 'r') as f:
        uzytkownicy = json.load(f)
        nowy_uzytkownik = {
            'id': len(uzytkownicy) + 1,
            'imie': imie,
            'email': email,
            'password': password,
        }
        uzytkownicy.append(nowy_uzytkownik)
        with open('uzytkownicy.json', 'w') as f:
            json.dump(uzytkownicy, f, indent=4)

@app.route('/wyniki_wyszukiwania_ksiazek', methods=['GET'])
def wyniki_wyszukiwania_ksiazek():
    tytul = request.args.get('tytul', '')
    autor = request.args.get('autor')
    isbn = request.args.get('isbn')
    with open('ksiazki.json', 'r') as file:
        books = json.load(file)
    wyniki = [book for book in books if (tytul.lower() in book['tytul'].lower() if tytul else True) and 
                                       (autor.lower() in book['autor'].lower() if autor else True) and 
                                       (isbn in book['isbn'] if isbn else True)]
    return render_template('wyniki_wyszukiwania_ksiazek.html', wyniki=wyniki)

@app.route('/wypozycz', methods=['POST'])
@login_required
def wypozycz():
    book_id = request.form['book_id']
    current_date = datetime.now().strftime('%Y-%m-%d')
    return_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
    with open('ksiazki.json', 'r') as file:
        books = json.load(file)
    with open('wypozyczenia.json', 'r') as file:
        wypozyczenia = json.load(file)
    for book in books:
        if book['id'] == int(book_id):
            if book['dostepnosc']:
                book['dostepnosc'] = False
                new_loan = {
                    "id": len(wypozyczenia) + 1,
                    "uzytkownik-id": current_user.id,
                    "ksiazka-id": int(book_id),
                    "wypozyczenie_data": current_date,
                    "zwrot_data": return_date
                }
                wypozyczenia.append(new_loan)
                with open('ksiazki.json', 'w') as file:
                    json.dump(books, file, indent=4)
                with open('wypozyczenia.json', 'w') as file:
                    json.dump(wypozyczenia, file, indent=4)
                flash('Książka została wypożyczona!', 'success')
                return redirect(url_for('wyniki_wyszukiwania_ksiazek'))
    flash('Nie udało się wypożyczyć książki.', 'danger')
    return redirect(url_for('wyniki_wyszukiwania_ksiazek'))

@app.route('/zwracanie', methods=['POST'])
@login_required
def zwracanie():
    book_id = request.form['book_id']
    with open('ksiazki.json', 'r') as file:
        books = json.load(file)
    with open('wypozyczenia.json', 'r') as file:
        wypozyczenia = json.load(file)
    for book in books:
        if book['id'] == int(book_id):
            if not book['dostepnosc']:
                # Sprawdzamy, czy aktualnie zalogowany użytkownik wypożyczył tę książkę
                loan_to_return = next((loan for loan in wypozyczenia if loan['ksiazka-id'] == int(book_id) and loan['uzytkownik-id'] == current_user.id), None)
                if loan_to_return:
                    book['dostepnosc'] = True
                    wypozyczenia.remove(loan_to_return)
                    with open('ksiazki.json', 'w') as file:
                        json.dump(books, file, indent=4)
                    with open('wypozyczenia.json', 'w') as file:
                        json.dump(wypozyczenia, file, indent=4)
                    flash('Książka została zwrócona!', 'success')
                    return redirect(url_for('wyniki_wyszukiwania_ksiazek'))
                else:
                    flash('Nie możesz zwrócić książki, której nie wypożyczyłeś.', 'danger')
                    return redirect(url_for('wyniki_wyszukiwania_ksiazek'))
    flash('Nie udało się zwrócić książki.', 'danger')
    return redirect(url_for('wyniki_wyszukiwania_ksiazek'))

if __name__ == '__main__':
    app.run(debug=True)
