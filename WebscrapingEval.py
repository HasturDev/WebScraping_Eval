from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
import pandas as pd
# initial url and list creation
session = webdriver.Chrome("chromedriver")
manufacturer_available = []
price = []
model = []
product_id = []
# Problem: change to an on_click() instead of calling the page by page number
for i in range(35):
    website = ('http://eval.arborian.com/?page=')
    session.get(website + str(i))
    # put in for page load times
    time.sleep(5)
    # scrape site by tags
    bs = BeautifulSoup(session.page_source, 'lxml')
    # Problem: find a way to split the small response into 2 lists before you finish the loop
    for i in bs.find_all('small'):
        manufacturer_available.append(i.get_text())
    for i in bs.find_all('b'):
        price.append(i.get_text())
    for i in bs.find_all('h3'):
        model.append(i.get_text())
    for i in bs.find_all('h3'):
        product_id.append(i.get('id'))
# create lists to split results of small tag into
manufacturer = []
available_product = []
for i in range(len(manufacturer_available)):
    if i % 2 == 0:
        manufacturer.append(manufacturer_available[i])
    else:
        available_product.append(manufacturer_available[i])
# create pandas dataframe with lists and place information into csv files
df = pd.DataFrame({'manufacturer': manufacturer,
                  'product_id': product_id,
                  'model': model,
                  'price': price,
                  "available product": available_product})  
# Problem: There is a better way to place this into a csv
# Possible_answer: maybe try having the str.match be a function def somefunc(i): .str.match[i]?
df[df['manufacturer'].str.match('By: Foo INC')].to_csv(r"C:\Users\i_miz\Documents\Visual_Studio_Projects\Prices.csv", index=False)
# Problem: want this to work without calling it as a seperate obj before making it a csv
someproduct_ids = df.loc[df['product_id'].isin(['198765', '382587', '251184', '127853', '601484', '699028', '261549', '750518']), ['product_id', 'price']]
someproduct_ids.to_csv(r"C:\Users\i_miz\Documents\Visual_Studio_Projects\Inventory_stuff.csv", index=False)