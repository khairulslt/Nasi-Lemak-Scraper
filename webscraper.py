import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time



# First Scraping Setup for LEE WEE BROTHERS NASI LEMAK
page = requests.get("https://leeweebrothers.com/our-food/lunch-boxes/#")
soup = BeautifulSoup(page.text, "html.parser")
# End of first Scraping Setup

# Scrape Lee Wee Brothers Nasi Lemak Website
print("\n\n====== LEE WEE BROTHERS NASI LEMAK ======")
divs = soup.find_all('div', {'style': 'max-height:580px;'})
names_and_prices = {
    # dict. sort by > name: price
    div.find('h2').text: div.find('span', {'class': 'amount'}).text.strip()
    for div in divs
}
for name, price in names_and_prices.items():
    print(("{: <50} {: >5}".format(name, price)).title()) # use .title to capitalize front letter of every word


# Second Scraping Setup for  JIA XIANG NASI LEMAK
page1 = requests.get("http://www.whattoeat.com.sg/jia-xiang-nasi-lemak")
soup1 = BeautifulSoup(page1.text, "html.parser")
# End of Second Scraping Setup

# Scrape Jia Xiang Nasi Lemak Website
print("\n\n====== JIA XIANG NASI LEMAK ======")
divs1 = soup1.find_all(True, {"id":["menuItemName55148", "menuItemName55150"]}) # find nasi lemak name
rest1 = soup1.find_all('span', {'class' : 'menu-item-price'}) # find price

for div1, a1 in zip(divs1, rest1):
    print("{: <50} {: >5}".format(div1.h3.text, a1.text)) # use "{: <50} {: >5}".format to give minimum width so price sorted into nice columns

# Thoughts: Did not use same method of scraping as lee wee brothers because Jia Xiangs site
# does not have all nasi lemak(s) under one div.