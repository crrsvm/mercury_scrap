from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'https://www.mercurymusic.cl/pianos-y-teclados?manufacturer=5477'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#PIANOS 

pi = soup.find_all('a', class_='product-item-link')
pianos = list()

count = 0
for i in pi:
    if count < 12:
        pianos.append(i.text)
    else:
        break
    count += 1

#PRECIOS

pr = soup.find_all('span', class_='price')

precios = list()

count = 0
for i in pr:
    if count < 12:
        precios.append(i.text)
    else:
        break
    count += 1

#print(precios)


df = pd.DataFrame({'Nombre': pianos, 'Precios':precios},  index=list(range(1,13)))
print(df, end=" ")


print(pianos)