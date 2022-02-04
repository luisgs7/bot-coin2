import requests
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

my_apikye = os.getenv("APIKYE") 


url = f'https://api.hgbrasil.com/finance?key={my_apikye}'

def price_dolar():
  data = requests.get(url).json()
  value = float(data["results"]["currencies"]["USD"]["buy"])
  value = format(value, '.2f')
  return value

def price_btc():
  data = requests.get(url).json()
  value = float(data["results"]["currencies"]["BTC"]["buy"])
  value = format(value, '.2f')
  return value

def price_eur():
  data = requests.get(url).json()
  value = float(data["results"]["currencies"]["EUR"]["buy"])
  value = format(value, '.2f')
  return value
