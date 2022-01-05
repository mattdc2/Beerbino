import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

#################################
### SCRAPING DU SITE "AUCHAN" ###
#################################

df_beer = pd.DataFrame(columns=["link_photo", "name", "brand", "price", "type"])
index = 0
nb_pages = 10

for page in range(1, nb_pages + 1) :
    url = "https://www.bieres.com/10-bieres?page=" + str(page)
    html = urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(html, features="lxml")
    divs_beer = soup.find_all("div", {"class": "item-product product_per_3 col-xs-12 col-sm-6 col-md-6 col-lg-4 col-xl-4"})

    for i in range(len(divs_beer)):
        div_beer = divs_beer[i]
        index += 1
        print(index)
        
        # Find beer's photo link
        div_photo = div_beer.find('img', {'class' : 'first-image'})
        link_beer_photo = div_photo['data-original']
        df_beer.at[index, "link_photo"] = link_beer_photo

        # Find beer's brand
        div_brand = div_beer.find("div", {"class": "manufacturer"})
        if div_brand != None :
            brand = div_brand.find('a').getText()
            df_beer.at[index, "brand"] = brand
        
        # Find beer's name
        div_name = div_beer.find("a", {"class": "product_name"})
        if div_name != None :
            name = div_name.getText()
            df_beer.at[index, "name"] = name
        
df_beer.to_csv("scraping_bierescom.csv")
