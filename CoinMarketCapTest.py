  #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'c46aafce-a49d-49f7-9a6c-bc4b951ea60e',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print("-------------------successfully connected to CoinMktCap-------------------")
  print("url: "+url)
  #print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)