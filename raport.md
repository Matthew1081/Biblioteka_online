1. Wstęp
Celem projektu było stworzenie prostego systemu zarządzania biblioteką online przy użyciu języka programowania Python i frameworka Flask. System umożliwia użytkownikom rejestrowanie się, logowanie, wyszukiwanie książek, wypożyczanie oraz zwracanie książek. Dodatkowo można dodawać nowych użytkowników i książki do bazy danych.

2. Technologie
Język programowania: Python
Framework: Flask
Baza danych: JSON (do przechowywania informacji o użytkownikach, książkach i wypożyczeniach)
Frontend: HTML, CSS
Biblioteka autoryzacji: Flask-Login
3. Funkcjonalności
Rejestracja użytkowników: Użytkownicy mogą się rejestrować, podając swoje dane.
Logowanie użytkowników: Użytkownicy mogą się logować, aby uzyskać dostęp do systemu.
Wyszukiwanie książek: Użytkownicy mogą wyszukiwać książki według tytułu, autora lub ISBN.
Wypożyczanie książek: Zalogowani użytkownicy mogą wypożyczać dostępne książki.
Zwracanie książek: Użytkownicy mogą zwracać książki, które wcześniej wypożyczyli.
Dodawanie książek: Można dodawać nowe książki do bazy danych.
Dodawanie użytkowników: Można dodawać nowych użytkowników.
4. Struktura projektu
aplikacja_webowa.py: Główny plik aplikacji Flask, zawiera wszystkie trasy oraz logikę biznesową.
templates/: Katalog zawierający szablony HTML.
index.html: Strona główna.
login_register.html: Strona logowania i rejestracji.
wyniki_wyszukiwania_ksiazek.html: Strona wyników wyszukiwania książek.
static/css/: Katalog zawierający pliki CSS.
main.css: Główny plik stylów.
uzytkownicy.json: Plik JSON przechowujący informacje o użytkownikach.
ksiazki.json: Plik JSON przechowujący informacje o książkach.
wypozyczenia.json: Plik JSON przechowujący informacje o wypożyczeniach.
5. Implementacja
Inicjalizacja aplikacji Flask: Stworzenie i konfiguracja aplikacji Flask, w tym ustawienie sekretu sesji oraz zainicjowanie Flask-Login.
Modele danych: Implementacja klasy User reprezentującej użytkownika oraz funkcji do ładowania użytkownika z pliku JSON.
Rejestracja i logowanie: Implementacja tras dla rejestracji i logowania użytkowników, w tym weryfikacja danych i zapisywanie użytkowników w pliku JSON.
Zarządzanie książkami: Implementacja tras dla dodawania, wyszukiwania, wypożyczania i zwracania książek, w tym aktualizacja dostępności książek oraz przechowywanie informacji o wypożyczeniach w pliku JSON.
Autoryzacja i autentykacja: Implementacja logiki autoryzacji i autentykacji użytkowników za pomocą Flask-Login, w tym ochrona tras wymagających zalogowania.
Powiadomienia: Dodanie powiadomień flash do informowania użytkowników o sukcesie lub błędach operacji takich jak logowanie, rejestracja, wypożyczanie czy zwracanie książek.
