from bs4 import BeautifulSoup
import requests
import re
gpu = input("enter the product you want ?")
url = f"https://www.newegg.com/p/pl?d={gpu}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page , "html.parser")


print(doc.prettify())
