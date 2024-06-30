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

6. Testy i problemy 
    Podczas testów wyszedł problem dotyczący wypożyczenia i zwracania książek (każdy użytkownik mógł wypożyczyć i zwrócić ksiązkę której nie wypożyczył) naprawione po przez dodanie dodatkowej weryfikacji jaka książka została wypożyczona przez którego użytkownika. Zostały dodane powiadomienia na stronie z komunikatami objaśniającymi błędy.
    problem html-owy chęć dodania rowijanego okienka w celu zalogowania się. Rozwiązano problem z okienkiem poprzez przekierowanie użutkownika na osobną podstronę dedykowaną do logowania i rejestracji.
    Problem informowanie użytkowników o wynikach operacji, takich jak logowanie, rejestracja, wypożyczanie i zwracanie książek.Rozwiązanie Użycie funkcji flash w Flask do wysyłania powiadomień do użytkowników oraz dodanie odpowiedniego kodu HTML i CSS do wyświetlania tych powiadomień w interfejsie użytkownika.
    Problem Walidacja danych wprowadzanych przez użytkowników oraz obsługa błędów, takich jak niepoprawne dane logowania czy brak uprawnień do wykonywania operacji. Rozwiązanie Walidacja danych w formularzach na poziomie serwera oraz wyświetlanie odpowiednich komunikatów błędów za pomocą powiadomień flash. Tutoriale na Real Python i dokumentacja Flask były tutaj pomocne.
    

1. Źródła
Flask
Oficjalna dokumentacja Flask:

Flask Documentation
Podstawowe informacje o Flask, konfiguracja, routing, szablony, zarządzanie sesjami i błędami.
Flask Mega-Tutorial:

Miguel Grinberg's Flask Mega-Tutorial
Kompletny przewodnik, który prowadzi przez cały proces tworzenia aplikacji internetowej przy użyciu Flask.
Flask Web Development (książka):

Flask Web Development by Miguel Grinberg
Książka zawiera szczegółowe omówienie Flask i jego zastosowań w projektach webowych.
Flask-Login
Dokumentacja Flask-Login:

Flask-Login Documentation
Zawiera informacje na temat autoryzacji, zarządzania sesjami użytkowników, implementacji logowania i wylogowywania.
Real Python: Flask-Login Tutorial:

Flask-Login Tutorial
Praktyczny przewodnik pokazujący, jak zintegrować Flask-Login z aplikacją Flask.
JSON
Dokumentacja JSON w Pythonie:

JSON Documentation
Oficjalna dokumentacja modułu JSON w Pythonie.
Real Python: Working with JSON:

Working with JSON in Python
Przewodnik po pracy z JSON w Pythonie, w tym czytanie i zapisywanie danych.
HTML i CSS
MDN Web Docs:

HTML
CSS
Dokumentacja i przewodniki po HTML i CSS, w tym podstawy, zaawansowane techniki, przykłady i najlepsze praktyki.
W3Schools:

HTML Tutorial
CSS Tutorial
Łatwo dostępne przewodniki i samouczki dla początkujących.
Python
Oficjalna dokumentacja Pythona:

Python Documentation
Dokumentacja standardowej biblioteki Pythona.
Real Python:

Real Python
Seria artykułów i samouczków na temat Pythona, w tym Flask, praca z JSON, zarządzanie plikami i wiele więcej.
