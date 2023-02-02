# Importing Modules

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

#Creating Data Frame for Scrapped Data
ScrappedData = pd.DataFrame()

#Scrapping Data from the webpages
for i in range(1,3):
    url = "https://www.flipkart.com/search?q=laptop+i5+11th+generation&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_3_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_3_6_na_na_na&as-pos=3&as-type=RECENT&suggestionId=laptop+i5+11th+generation%7CLaptops&requestId=ffd8af64-5e3c-47d7-870e-7265c4df4d42&as-searchtext=laptop&p%5B%5D=facets.price_range.from%3D40000&p%5B%5D=facets.price_range.to%3D50000&p%5B%5D=facets.processor%255B%255D%3DCore%2Bi5&page={}".format(i)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

    response = requests.request("GET", url, headers=headers).text
    
    # Parsing the collected data
    soup = BeautifulSoup(response, 'lxml')
    #Storing the parsed data in a list
    lapList = soup.find_all('div', class_ = '_2kHMtA')
    
    lapName = []
    lapRating = []
    lapPrice = []

    for j in lapList :
        lapName.append(j.find_all('div', class_ = '_4rR01T')[0].text)
        lapPrice.append(j.find_all('div', class_ = '_30jeq3 _1_WHN1')[0].text)
        try :
            lapRating.append(j.find_all('div', class_ = '_3LWZlK')[0].text)
        except:
            lapRating.append(np.nan)
    lapdict = {'Name' : lapName, "Ratings" : lapRating, "Price" : lapPrice}
    # Chaning the data from a list to a dataframe
    Laptops = pd.DataFrame(lapdict)
    # Appending all the dataframes into a single dataframe
    ScrappedData = ScrappedData.append(Laptops, ignore_index=True)
    
    
# Converting the dataframe into a csv file

ScrappedData.to_csv("FlipkartScrappedData.csv")
