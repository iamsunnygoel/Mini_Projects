import yfinance as yf

ticker = yf.Ticker("RELIANCE.NS")
data = ticker.history(period="1d", interval="1m")
print(data.tail())  # Recent prices
print(ticker.info['regularMarketPrice'])  # Current price


api_key=...