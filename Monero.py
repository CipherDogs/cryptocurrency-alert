import requests
import time
crypto_wallet = input('Crypto_wallet:')
if crypto_wallet != '':
  r = requests.get('https://api.cryptonator.com/api/ticker/' + crypto_wallet + '-usd')
  data = r.json()
  price = data ['ticker']['price']
  change = data ['ticker']['change']
  while True:
    print(crypto_wallet,'=',price,"USD")
    print("change = ",change)
    time.sleep(120)
else :
  print("error")
