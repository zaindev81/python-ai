from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# height
X = np.array([150, 155, 160, 165, 170, 175]).reshape(-1, 1)

# weight
y = np.array([25, 32, 40, 46, 55, 62])

model = LinearRegression()
model.fit(X, y)

print("Coefficient:", model.coef_, "Intercept:", model.intercept_)

y_pred = model.predict(X)

# Plotting the data points and the fitted line
plt.scatter(X, y, color="blue", label="Actual data")
plt.plot(X, y_pred, color="red", label="Regression line")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Relationship between Height and Weight")
plt.legend()
plt.grid(True)
plt.show()