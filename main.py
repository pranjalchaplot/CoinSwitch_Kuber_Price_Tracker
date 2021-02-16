from bs4 import BeautifulSoup
from selenium import webdriver
import smtplib
import requests
import pandas as pd
import json
import time


def getCryptoPrice(num):
    cryptoText = {
        0: "BTC",
        1: "ETH",
        2: "XRP",
        3: "TRX",
        4: "USDT",
        5: "LTC",
        6: "DASH",
    }
    URL = 'https://coinswitch.co'

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)

    time.sleep(6)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')

    price = soup.select(
        '.kuber .kuber-header__container .container .ticker .ticker__item .ticker__price')[num].text

    print(cryptoText[num] + " Buy Price is: " + str(price))


# Choose A Num to Get the Crypto Details from CoinSwitch Kuber in INR.
# Use BTC : 0, ETH : 1, XRP : 2, TRX : 3, USDT : 4, LTC : 5, DASH : 6
# For Ex, num = 0 Will Give Details for BTC which is set by default.
num = 0

# Run the Price Check Function
getCryptoPrice(num)
