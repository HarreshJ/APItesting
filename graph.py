import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

# Replace 'AAPL' with the stock ticker you want to analyze
aapl_stock_data = yf.download('AAPL', start='2023-01-01', end='2024-07-24')
goog_stock_data = yf.download('GOOG', start='2023-01-01', end='2024-07-24')
amzn_stock_data = yf.download('AMZN', start='2023-01-01', end='2024-07-24')
msft_stock_data = yf.download('MSFT', start='2023-01-01', end='2024-07-24')
nvda_stock_data = yf.download('NVDA', start='2023-01-01', end='2024-07-24')
orcl_stock_data = yf.download('ORCL', start='2023-01-01', end='2024-07-24')

# Convert the index to a datetime object
aapl_stock_data.index = pd.to_datetime(aapl_stock_data.index)
goog_stock_data.index = pd.to_datetime(goog_stock_data.index)
msft_stock_data.index = pd.to_datetime(msft_stock_data.index)
amzn_stock_data.index = pd.to_datetime(amzn_stock_data.index)
orcl_stock_data.index = pd.to_datetime(orcl_stock_data.index)

plt.figure(figsize=(12, 6))
plt.plot(aapl_stock_data['Close'], label='AAPL')
plt.plot(goog_stock_data['Close'], label='GOOG')
plt.plot(amzn_stock_data['Close'], label='AMZN')
plt.plot(msft_stock_data['Close'], label='MSFT')
plt.plot(nvda_stock_data['Close'], label='NVDA')
plt.plot(orcl_stock_data['Close'], label='ORCL')


plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Tech companies stock price')
plt.legend()
plt.grid(True)
plt.show()