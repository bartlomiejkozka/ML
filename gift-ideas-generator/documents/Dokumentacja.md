# **Dokumentacja użytkownika – Gift Ideas Generator**
## **1. Opis aplikacji**
Gift Ideas Generator to aplikacja desktopowa oparta na dużym modelu językowym (LLM), która umożliwia generowanie unikalnych pomysłów na prezenty na podstawie opisu odbiorcy. Użytkownik wpisuje kilka informacji o osobie, dla której szuka prezentu, takich jak:

- Wiek
- Płeć
- Kim jest dla ciebie?
- Budżet(z uwzględnieniem waluty)
- Zainteresowania 
- Okazja 

Aplikacja przy użyciu modelu Gemini zwraca gotowe sugestie.

## **2. Struktura projektu**
gift-ideas-generator/

├── documents/              # Dokumentacja

├── geminiAPI.py            # Komunikacja z Gemini API

├── gui.py                  # Główna aplikacja GUI 

├── requirements.txt        # Lista potrzebnych bibliotek

└── README.md               # Opis instalacji, konfiguracji i uruchomienia

## **3. Funkcjonalności**
\- Interfejs graficzny GUI oparty na Tkinter, biblioteki pozwalającej na stworzenie prostego i intuicyjnego interfejsu dla użytkownika

\- Integracja z API Google Gemini, to połączenie umożliwia wykorzystanie zaawansowanych możliwości przetwarzania języka naturalnego i generowania odpowiedzi

\- Obsługa promptów wpisywanych przez użytkownika, które aplikacja przekazuje do modelu 
## **4. Technologie użyte w projekcie**
\- Python 3.8+

\- Tkinter (GUI)

\- Google Gemini API

\- Obsługa plików .env do bezpiecznego przechowywania klucza API
## **5. Wymagania techniczne**
\- System operacyjny: Windows / macOS / Linux

\- Python w wersji co najmniej 3.8

\- Biblioteki z pliku requirements.txt

\- Klucz API Gemini (do umieszczenia w pliku .env)


