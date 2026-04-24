from bs4 import BeautifulSoup
import requests

search = input("enter the product you want ? ")
pg_no = int(input("enter the page number : "))

url = f"https://www.newegg.com/p/pl?N=4131&d={search}&page={pg_no})"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

print(doc.prettify())
