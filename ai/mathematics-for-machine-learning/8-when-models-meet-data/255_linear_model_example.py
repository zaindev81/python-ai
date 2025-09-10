# 255
import numpy as np

# --- 1. One-dimensional linear model (y = ax + b) ---
# Example: House area (m^2) and price (in 10,000 yen)
a = 3.5   # Price per 1 m^2
b = 50    # Base price
x_1d = np.array([30, 50, 80])  # House areas
y_1d = a * x_1d + b
print("Predicted prices (1D model):", y_1d)

# --- 2. Multi-dimensional linear model (y = w1*x1 + w2*x2 + w3*x3 + b) ---
# Features: [Area (m^2), Distance to station (km), Age of building (years)]
# Weights (impact on price)
w = np.array([3.5, -2.0, -1.0])  # Larger area ↑, farther station ↓, older building ↓
b = 50

# House feature data (3 houses)
X = np.array([
    [30, 1.0, 5],   # Small house, near station, relatively new
    [50, 3.0, 10],  # Medium house, far from station, old
    [80, 0.5, 2]    # Large house, very near station, very new
])

# Predictions for multi-dimensional model
y_multidim = X @ w + b  # Dot product + bias
print("Predicted prices (Multi-dimensional model):", y_multidim)

# --- 3. Vector notation (y = w^T x + b) check ---
# Example: First house
x1 = X[0]
y1 = w.T @ x1 + b
print("Prediction for first house (vector form):", y1)
