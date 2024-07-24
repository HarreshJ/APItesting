import yfinance as yf

# Get data for Apple
apple = yf.Ticker("AAPL")

# Get historical prices
apple_history = apple.history(period="6mo")

# Print the closing prices
print(apple_history['Close'])
