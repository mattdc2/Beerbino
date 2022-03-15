import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import urllib.request

####################################################
### FUNCTION TO DOWNLOAD ALL IMAGES FROM WEBSITE ###
####################################################

def download_image(df, path) :
    for index, row in df.iterrows() :
        link = row['link_photo']
        complete_path = path + str(index) + '.jpg'
        print(complete_path)

        urllib.request.urlretrieve(link, complete_path)

df = pd.read_excel(r'./data_beers.xlsx')
download_image(df, './data/images/')