import requests
import pandas as pd

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
stockNames = ['AAPL', 'GOOG', 'MSFT', 'INTC', 'AMZN']

for i in range(len(stockNames)):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stockNames[i]}&interval=60min&apikey=redundantorigins'
    r = requests.get(url)
    data = r.json()
    df = pd.DataFrame(data)
    print(df)