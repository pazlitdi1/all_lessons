import requests


url = 'https://api.binance.com/api/v3/ticker/price'

response = requests.get(url, params={'symbol': 'BTCUSDT'})

# price = response.json()
price_object = response.json()
price = float(price_object['price'])
print(price)

