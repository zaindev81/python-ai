import yfinance as yf

ticker = "GOOGL"
data = yf.download(ticker, start="2024-01-01", end="2024-07-01", interval="1wk")

print(data.head())
print("Latest Close Price:", data["Close"].iloc[-1])