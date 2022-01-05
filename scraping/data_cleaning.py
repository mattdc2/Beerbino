import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import urllib.request

df_auchan = pd.read_csv(r'./scraping_auchan.csv')
df_saveurbiere = pd.read_csv(r'./scraping_saveurbiere.csv')
df_bierescom = pd.read_csv(r'./scraping_bierescom.csv')

df_auchan['website'] = 'Auchan'
df_saveurbiere['website'] = 'SaveurBiere'
df_bierescom['website'] = 'BieresCom'

df = pd.concat([df_auchan, df_bierescom, df_saveurbiere])
df.reset_index(inplace=True)
df.drop(columns=['link_photo', 'Unnamed: 0', 'index'], inplace=True)
print(df)

df.to_excel(r'./data_beers.xlsx')