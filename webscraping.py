import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
response = requests.get(url)

#print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)

quotes = soup.find_all("div", class_="quote")



with open("autores.txt", "w", encoding="utf-8") as archivo:

    print("Autores de citas")
    for quote in quotes:
        autor = quote.find("small", class_="author").text
        print(autor)
        archivo.write(autor + "\n")

