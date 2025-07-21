from bs4 import BeautifulSoup
import requests
import os

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

if os.path.exists("last_page.txt"):
    with open("last_page.txt", "r") as f:
        page = int(f.read().strip()) + 1
else:
    page = 1

with open("books.txt", "a", encoding="utf-8") as file:
    while True:
        URL = base_url.format(page)
        try:
            response = requests.get(URL, timeout=10)
            response.encoding = 'utf-8'
        except requests.exceptions.RequestException as e:
            print(f'Failed to load page {page}: {e}')
            break

        if response.status_code != 200:
            print(f'Page {page} does not exist.')
            break

        soup = BeautifulSoup(response.text, 'html.parser')

        print(f'\nPage {page}')
        print(f'{"Title":<100}{"Price":<10}')
        print('-' * 140)

        file.write(f'\n\n{"="*60} Page {page} {"="*60}\n')
        file.write(f'{"Title":<100}{"Price":<10}\n')
        file.write('-' * 140 + '\n')

        for book in soup.find_all('article', class_='product_pod'):
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').string
            print(f'{title:<100}{price:<10}')
            file.write(f'{title:<100}{price:<10}\n')

        with open("last_page.txt", "w") as f:
            f.write(str(page))

        next_page = input("Show next page? (Yes or No): ")
        if next_page.lower() != "yes":
            break

        page += 1
