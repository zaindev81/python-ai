from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Working time (hours)
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

# Progress (%)
y = np.array([15, 30, 45, 60, 78, 95])

model = LinearRegression()
model.fit(X, y)

print("Slope:", model.coef_[0], "Intercept:", model.intercept_)

y_pred = model.predict(X)

plt.scatter(X, y, color="blue", label="Actual data")
plt.plot(X, y_pred, color="red", label="Regression line")
plt.xlabel("Working time (hours)")
plt.ylabel("Progress (%)")
plt.title("Relationship between time and progress")
plt.legend()
plt.grid(True)
plt.show()