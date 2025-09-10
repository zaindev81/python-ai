import pandas as pd

data = pd.DataFrame({
    "Open": [100, 102, 104],
    "Close": [101, 103, 105]
}, index=["2025-09-01", "2025-09-02", "2025-09-03"])

print(data)

# 2.1 Select a Row by Position
print(data.iloc[0])  # First row
print(data.iloc[1])  # Second row
print(data.iloc[-1])  # Negative index = count from the end