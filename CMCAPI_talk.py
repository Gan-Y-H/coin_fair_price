  #This example uses Python 2.7 and the python-request library.

import requests
from urllib import request
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

# latest listing data
url_latest_listing = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'c46aafce-a49d-49f7-9a6c-bc4b951ea60e',
}

# historical listing data
# Alpha Vantage API key: 8YHJEZ783X86EHRR
hist_url_list = []
# BTC
btc_url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey=8YHJEZ783X86EHRR'
hist_url_list.append(btc_url)

#ETH
eth_url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=ETH&market=USD&apikey=8YHJEZ783X86EHRR'
hist_url_list.append(eth_url)

#SOL
sol_url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=SOL&market=USD&apikey=8YHJEZ783X86EHRR'
hist_url_list.append(sol_url)

#ADA (cardano)
ada_url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=ADA&market=USD&apikey=8YHJEZ783X86EHRR'
hist_url_list.append(ada_url)

#AVAX
avax_url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=AVAX&market=USD&apikey=8YHJEZ783X86EHRR'
hist_url_list.append(avax_url)

session = Session()
session.headers.update(headers)

try:
  # historical listing data
  hist_data = []
  # hist_data is a list that contains data of each crypto coin in dictionary
  for url in hist_url_list:
    hist_data.append(requests.get(url).json())
  print("-------------------successfully connected to AlphaVantage-------------------")
  # print(hist_data)

  # lastest listing data
  response = session.get(url_latest_listing, params=parameters)
  latest_data = json.loads(response.text)
  print("-------------------successfully connected to CoinMktCap-------------------")
  print("url: "+url_latest_listing)
  #print(latest_data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)