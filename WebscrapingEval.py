from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
import pandas as pd
#initial url and BS4 Usage
session = webdriver.Chrome("chromedriver")
manufacturer_available = []
price = []
model = []
product_id = []
for i in range(35):
    website = ('http://eval.arborian.com/?page=')
    session.get(website + str(i))
    time.sleep(5)
    bs = BeautifulSoup(session.page_source, 'lxml')
    for i in bs.find_all('small'):
        manufacturer_available.append(i.get_text())
    for i in bs.find_all('b'):
        price.append(i.get_text())
    for i in bs.find_all('h3'):
        model.append(i.get_text())
    for i in bs.find_all('h3'):
        product_id.append(i.get('id'))
manufacturer = []
available_product = []
for i in range(len(manufacturer_available)):
    if i % 2 == 0:
        available_product.append(manufacturer_available[i])
    else:
        manufacturer.append(manufacturer_available[i])
df = pd.DataFrame({'manufacturer': available_product,
                  'product id': product_id,
                  'model': model,
                  'price': price,
                  "available product": manufacturer})
df[df['manufacturer'].str.match('By: Foo INC')].to_csv(r"C:\Users\i_miz\Documents\Visual_Studio_Projects\Webscraper.csv", index=False)
df[df.index.isin([45, 49, 112, 137, 141, 155, 160, 168, 172])].to_csv(r"C:\Users\i_miz\Documents\Visual_Studio_Projects\Id.csv", index=False)
