import yfinance as yf
import pandas as pd

# Get data for Apple
apple = yf.Ticker("AAPL")

# Get historical prices
apple_history = apple.history(period="6mo")

# Print the closing prices
data = apple_history['Close']

df = pd.DataFrame(data=data)

print(df)