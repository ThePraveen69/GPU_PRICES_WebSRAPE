from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time 
path = r"C:\Users\ADMIN\.wdm\drivers\chromedriver\win64\147.0.7727.117\chromedriver-win32\chromedriver.exe"
service = Service(path)
driver =webdriver.Chrome(service=service) 


page_url = f"https://www.newegg.com/p/pl?N=4131&d=3080&page=1)"
driver.get(page_url)
time.sleep(20)
html = driver.page_source
doc = BeautifulSoup(html , "html.parser")

print(doc.prettify())
