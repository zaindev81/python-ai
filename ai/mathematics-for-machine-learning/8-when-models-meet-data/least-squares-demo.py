# least_squares_demo.py
# Implement least squares (MSE minimization) in NumPy and compare OLS (closed form) vs. Gradient Descent

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)

# 1) Generate data: y = 3x + 2 + noise
N = 100
X = rng.random((N, 1))                   # shape: (N, 1)
true_w, true_b = 3.0, 2.0
y = true_w * X[:, 0] + true_b + 0.2 * rng.normal(size=N)

# 2) Loss (MSE) and helpers
def predict(w, b, x):
    return w * x + b

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# 3) OLS (closed-form): beta = (X^T X)^(-1) X^T y
#    This solves for the parameter that minimizes the mean loss in one shot.
X_design = np.column_stack([np.ones(N), X[:, 0]])  # [1, x]
beta, *_ = np.linalg.lstsq(X_design, y, rcond=None)
ols_b, ols_w = beta[0], beta[1]

# 4) Gradient Descent (ERM procedure to minimize MSE)
w, b = 0.0, 0.0
lr = 0.05
epochs = 1500
hist = []

for _ in range(epochs):
    y_hat = predict(w, b, X[:, 0])
    # Gradients of R_emp = (1/N) Σ (y - ŷ)^2
    grad_w = (-2.0 / N) * np.sum((y - y_hat) * X[:, 0])
    grad_b = (-2.0 / N) * np.sum((y - y_hat))
    w -= lr * grad_w
    b -= lr * grad_b
    hist.append(mse(y, predict(w, b, X[:, 0])))

# 5) Results
print("[True] w=%.3f, b=%.3f" % (true_w, true_b))
print("[OLS ] w=%.3f, b=%.3f, MSE=%.4f" % (ols_w, ols_b, mse(y, predict(ols_w, ols_b, X[:, 0]))))
print("[GD  ] w=%.3f, b=%.3f, MSE=%.4f" % (w, b, mse(y, predict(w, b, X[:, 0]))))

# 6) Visualization
# Learning curve (MSE over epochs)
plt.figure(figsize=(6,4))
plt.plot(hist)
plt.xlabel("Epoch")
plt.ylabel("Empirical Risk (MSE)")
plt.title("Learning Curve (Gradient Descent)")
plt.tight_layout()
plt.show()

# Fit (data points + regression lines)
x_plot = np.linspace(0, 1, 200)
plt.figure(figsize=(6,4))
plt.scatter(X[:, 0], y, label="Data")
plt.plot(x_plot, predict(ols_w, ols_b, x_plot), label="OLS (closed-form)")
plt.plot(x_plot, predict(w, b, x_plot), label="Gradient Descent")
plt.xlabel("x"); plt.ylabel("y"); plt.title("Least Squares Fit")
plt.legend(); plt.tight_layout(); plt.show()
