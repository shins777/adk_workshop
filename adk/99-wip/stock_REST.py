import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=GOOG&interval=5min&apikey=CBPHIO7CGA890ZMA'
r = requests.get(url)
data = r.json()

print(data)