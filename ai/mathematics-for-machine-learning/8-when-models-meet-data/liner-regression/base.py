from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

"""
This code is a simple example of supervised learning (regression),
where you create your own linear data, train a model on it,
and check how accurately the model can estimate the original linear equation.
"""

# np.random.seed(0)

X = np.random.rand(100, 1) # a feature matrix with a shape of [100, 1]
y = 3 * X[:, 0] + 2 + 0.1 * np.random.randn(100) # y=3x+2+noise

model = LinearRegression()
model.fit(X, y) # Least squares method


# Finds the best-fitting line for the data using the least squares method.
# It estimates the slope (coefficient) and intercept.

print("Coefficient:", model.coef_, "Intercept:", model.intercept_)

# model.coef_: The slope(s) of the fitted line.
# model.intercept_: The intercept of the fitted line.
# Since we generated data with y = 3x + 2 + noise, the model should output values close to 3 and 2.

# Coefficient: [3.01] Intercept: 2.00
# meaning the fitted line is roughly:
# y≈3.01x+2.00

# Predicted values of the regression line
y_pred = model.predict(X) # Calculate the predicted y values corresponding to X using the trained model.

# R² (coefficient of determination)
# The value ranges from 0 to 1 (the closer to 1, the better the prediction).
# A score of 0.95 or higher indicates a very good prediction, while a score of 0.5 or lower suggests low accuracy.
r2 = r2_score(y, y_pred) # Calculate the R² score.
print("R² score:", r2)

# MSE (Mean Squared Error)
# The average of the squared differences between the predicted values and the actual values.
# The smaller the value, the better (a value close to 0 indicates a perfect fit).
mse = mean_squared_error(y, y_pred)
print("MSE:", mse)


# Plotting
plt.figure(figsize=(6, 4))
plt.scatter(X, y, color="blue", label="Data (with noise)")
plt.plot(X, y_pred, color="red", linewidth=2, label="Fitted line")
plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Regression Fit")
plt.legend()
plt.grid(True)
plt.show()