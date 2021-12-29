import requests


def price_dolar():
  data = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL").json()
  value = float(data["USDBRL"]["high"])
  date_time = data["USDBRL"]["create_date"]
  value = round(value, 3)
  return (value, date_time)

def price_btc():
  data = requests.get("https://economia.awesomeapi.com.br/json/last/BTC-BRL").json()
  value = float(data["BTCBRL"]["bid"])
  date_time = data["BTCBRL"]["create_date"]
  value = round(value, 3)
  return (value, date_time)

def price_eth():
  data = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=ETHBRL").json()
  value = float(data["price"])
  return value
