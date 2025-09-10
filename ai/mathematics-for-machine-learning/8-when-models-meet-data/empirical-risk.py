import numpy as np

# True values (y) and model predictions (y_hat)
y_true = np.array([3.0, 5.0, 2.0])
y_pred = np.array([2.5, 4.0, 2.5])

# Loss function (Squared Error)
losses = (y_true - y_pred) ** 2
print("Loss for each data point:", losses)

# Mean loss (Empirical Risk)
empirical_risk = np.mean(losses)
print("Mean loss (Empirical Risk):", empirical_risk)
