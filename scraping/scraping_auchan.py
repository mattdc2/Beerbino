import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

#################################
### SCRAPING DU SITE "AUCHAN" ###
#################################

df_beer = pd.DataFrame(columns=["link_photo", "name", "brand", "type"])
index = 0
nb_pages = 20

for page in range(1, nb_pages + 1) :
    url = "https://www.auchan.fr/boissons/bieres-alcools-aperitifs/cave-a-bieres/ca-n070704?page=" + str(page)
    html = urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(html, features="lxml")
    divs_beer = soup.find_all("article", {"class": "product-thumbnail list__item shadow--light product-thumbnail--column outOfStock"})

    for i in range(len(divs_beer)):
        div_beer = divs_beer[i]
        index += 1
        print(index)
        
        # Find beer's photo link
        div_photo = div_beer.find('meta')
        link_beer_photo = div_photo['content']
        df_beer.at[index, "link_photo"] = link_beer_photo

        # Find beer's brand
        div_brand = div_beer.find("strong", {"itemprop": "brand"})
        if div_brand != None :
            brand = div_brand.getText()
            df_beer.at[index, "brand"] = brand
        
        # Find beer's name
        div_name = div_beer.find("p", {"itemprop": "name description"})
        name0 = div_name.contents
        if len(name0) >= 2:
            name = div_name.contents[1].strip()
            df_beer.at[index, "name"] = name

        # Find beer's attribute
        div_type = div_beer.find("span", {"class": "product-attribute"})
        if div_type != None :
            if len(div_type) >= 2 :
                df_beer['type'] = 'TO_DELETE'
            else :
                type = div_type.contents[0]
                print(type)
                if type not in ['25cl', '33cl', '37,5cl', '50cl', '75cl', '1,5L', '1L'] :
                    df_beer['type'] = 'TO_DELETE'
        
df_beer.to_csv("scraping_auchan.csv")
