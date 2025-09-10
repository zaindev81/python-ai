import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Download the data (last 2 years)
# Use auto_adjust=False to avoid the warning and get consistent column structure
apple_data = yf.download("AAPL", start="2023-01-01", end="2025-01-01", auto_adjust=False)
sp500_data = yf.download("^GSPC", start="2023-01-01", end="2025-01-01", auto_adjust=False)

# Extract Adj Close - handle MultiIndex columns properly
apple = apple_data["Adj Close"]
sp500 = sp500_data["Adj Close"]

# 2. Compute daily returns
apple_ret = apple.pct_change().dropna()
sp500_ret = sp500.pct_change().dropna()

# 3. Combine the datasets and drop missing values
data = pd.concat([apple_ret, sp500_ret], axis=1)
data.columns = ["apple", "sp500"]
data = data.dropna()

# 4. Linear regression (CAPM: Apple return ~ α + β * Market return)
X = data[["sp500"]].values
y = data["apple"].values

model = LinearRegression().fit(X, y)
alpha = model.intercept_
beta = model.coef_[0]

print(f"Alpha (excess return): {alpha:.6f}")
print(f"Beta (market sensitivity): {beta:.4f}")

# Optional: Print some additional statistics
print(f"\nData points used: {len(data)}")
print(f"R-squared: {model.score(X, y):.4f}")
print(f"Average daily return - Apple: {data['apple'].mean():.4f}")
print(f"Average daily return - S&P 500: {data['sp500'].mean():.4f}")
print(f"Volatility - Apple: {data['apple'].std():.4f}")
print(f"Volatility - S&P 500: {data['sp500'].std():.4f}")