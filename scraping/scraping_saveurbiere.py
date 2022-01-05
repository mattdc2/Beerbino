import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

###########################################
### SCRAPING DU SITE "saveur-biere.com" ###
###########################################

df_beer = pd.DataFrame(columns=["link_photo", "name", "brand"])
index = 0
nb_pages = 1

for page in range(1, nb_pages + 1) :
    url = "https://www.saveur-biere.com/fr/3-bouteilles" + "/p-" + str(page)
    html = urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(html, features="lxml")
    divs_beer = soup.find_all("div", {"class": "styled__Container-sc-18z0658-0 eJfVwm"})

    for i in range(len(divs_beer)) :
        div_beer = divs_beer[i]
        index += 1

        # Find beer's photo link
        div_photo = div_beer.find("div", {"class": "styled__Wrapper-zk0hmv-0 ebkvGG"})
        link_beer_photo = div_photo.contents[1]['srcset'].split(" ")[0]
        df_beer.at[index, "link_photo"] = link_beer_photo

        # Find beer's name
        div_name = div_beer.find("a", {"class": "styled__Element-k8ouqn-0 drfDsq styled__Name-sc-18z0658-5 hgVXwa"})
        name = div_name.getText()
        df_beer.at[index, "name"] = name

        # Find beer's brand
        div_brand = div_beer.find("a", {"class": "styled__Element-k8ouqn-0 drfDsq styled__Brewery-sc-18z0658-7 blBvcc"})
        brand = div_brand.getText()
        df_beer.at[index, "brand"] = brand

        '''
        # Find beer's type
        div_type = div_beer.find("a", {"class": "styled__Button-sc-15rjfzq-1 fYEjow"})
        type = div_type.getText()
        df_beer.at[index, "type"] = type

        # Find beer's price
        div_price = div_beer.find("p", {"class": "Heading-hec8nf-0 styled__Price-sc-93ovya-2 lonnpE gKXohr"})
        if div_price == None :
            div_price = div_beer.find("p", {"class": "Heading-hec8nf-0 styled__Price-sc-126vld9-2 lonnpE npVHJ"})
        price = div_price.getText()
        df_beer.at[index, "price"] = price[:-1]'''

df_beer.to_csv("scraping_saveurbiere.csv")
