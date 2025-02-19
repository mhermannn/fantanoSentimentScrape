# FantanoScraper

## Struktura folderów projektu

### Folder `albums`

W folderze `albums` znajdują się różne pobrane przeze mnie albumy. W prezentacji korzystałam z następujących albumów:

- Preacher's Daughter
- BRAT
- Vultures 1
- TPAB
- Speedin Bullet 2 Heaven

### Folder `scraping`

Folder `scraping` zawiera pliki do pobierania danych dotyczących albumów. Wykorzystuję do tego YouTube Data API v3, które wymaga wygenerowania własnego klucza. Można to zrobić tutaj: [Google Cloud Console](https://console.cloud.google.com/marketplace/product/google/youtube.googleapis.com?q=search&referrer=search&hl=pl&project=shaped-plateau-426211-h4).

Mój klucz znajduje się w pliku o nazwie `key.txt` w folderze głównym i w tym miejscu szukają go funkcje znajdujące się w folderze `scraper`.

### Folder `sentiment`

Folder `sentiment` zawiera funkcje dotyczące analizy tekstowej oraz tworzenia odpowiednich wykresów.

### Plik `main.py`

Plik `main.py` zawiera listę albumów do pobrania i jest używany do uruchamiania całego projektu.

### Plik `organizer.py`

Plik `organizer.py` służy do odpowiedniego pobierania i zapisywania informacji dla danego albumu.
