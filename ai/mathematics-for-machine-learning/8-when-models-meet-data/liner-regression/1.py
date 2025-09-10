from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Prediction of the relationship between sales and advertising expenses

# advertising expenses
X = np.array([10, 15, 20, 25, 30, 35]).reshape(-1, 1) # Convert the array into a "rows × columns" format.
print("X", X)

# sales
y = np.array([25, 32, 40, 46, 55, 62])

model = LinearRegression()
model.fit(X, y)

print("Coefficient:", model.coef_, "Intercept:", model.intercept_)

y_pred = model.predict(X)

# Plotting the data points and the fitted line
plt.scatter(X, y, color="blue", label="Actual data")
plt.plot(X, y_pred, color="red", label="Regression line")
plt.xlabel("Advertising Expenses")
plt.ylabel("Sales")
plt.title("Relationship between Sales and Advertising Expenses")
plt.legend()
plt.grid(True)
plt.show()