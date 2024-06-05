import tkinter as tk
from tkinter import messagebox
import json

def dodaj_ksiazke(tytul, autor, isbn):
    with open('ksiazki.json', 'r') as f:
        ksiazki = json.load(f)

    nowa_ksiazka = {
        'id': len(ksiazki) + 1,
        'tytul': tytul,
        'autor': autor,
        'isbn': isbn,
        'available': True,
        
    }

    ksiazki.append(nowa_ksiazka)

    with open('ksiazki.json', 'w') as f:
        json.dump(ksiazki, f, indent=4)

def dodawanie_ksiazki_gui():
    def submit():
        tytul = tytul_entry.get()
        autor = autor_entry.get()
        isbn = isbn_entry.get()
        dodaj_ksiazke(tytul, autor, isbn)
        messagebox.showinfo('Dodawanie ksiazki', 'Ksiazka dodana poprawnie')

    okno = tk.Tk()
    okno.title('Dodawanie ksiazki')

    tk.Label(okno, text='Tytul:').pack()
    tytul_entry = tk.Entry(okno)
    tytul_entry.pack()

    tk.Label(okno, text='Autor:').pack()
    autor_entry = tk.Entry(okno)
    autor_entry.pack()

    tk.Label(okno, text='ISBN:').pack()
    isbn_entry = tk.Entry(okno)
    isbn_entry.pack()

    tk.Button(okno, text='Dodaj', command=submit).pack()

    okno.mainloop()

dodawanie_ksiazki_gui()



    