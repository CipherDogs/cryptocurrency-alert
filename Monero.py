import requests
import time
r = requests.get('https://api.cryptonator.com/api/ticker/xmr-usd')
data = r.json()
price = data ['ticker']['price']
change = data ['ticker']['change']
while True:
  print("XMR = ",price,"USD")
  print("Change = ",change)
  time.sleep(60)