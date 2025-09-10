# ERM (Empirical Risk Minimization) — Regression + MSE
# ① Define the loss function → ② Compute the mean loss (empirical risk)
# → ③ Minimize it (Gradient Descent)

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)

# ── Create data (a subset of the population = training data)
N = 100
X = rng.random((N, 1))                    # shape (N,1)
true_w, true_b = 3.0, 2.0
y = true_w * X[:, 0] + true_b + 0.2 * rng.normal(size=N)

# ── ① Loss function (per-sample error): MSE component (y - ŷ)^2
def predict(w, b, x):        # prediction function f(x;θ)
    return w * x + b

def per_sample_loss(y_true, y_pred):
    return (y_true - y_pred) ** 2

# ── ② Empirical risk (mean loss): average over all data
def empirical_risk(w, b, x, y_true):
    y_hat = predict(w, b, x)
    return np.mean(per_sample_loss(y_true, y_hat))

# ── ③ Minimization: use gradient descent to find θ = (w,b) that reduces R_emp
w, b = 0.0, 0.0            # initial values
lr = 0.05                  # learning rate
epochs = 1500
history = []

x1 = X[:, 0]
for _ in range(epochs):
    y_hat = predict(w, b, x1)
    # Gradient of R_emp = (1/N) Σ (y - ŷ)^2 w.r.t. w and b
    grad_w = (-2.0 / N) * np.sum((y - y_hat) * x1)
    grad_b = (-2.0 / N) * np.sum((y - y_hat))
    w -= lr * grad_w
    b -= lr * grad_b
    history.append(empirical_risk(w, b, x1, y))

print(f"[ERM - GD] w={w:.4f}, b={b:.4f}, R_emp={history[-1]:.6f}")

# Reference: closed-form (OLS) solution for comparison
X_design = np.column_stack([np.ones(N), x1])
beta, *_ = np.linalg.lstsq(X_design, y, rcond=None)
ols_b, ols_w = beta[0], beta[1]
print(f"[OLS]      w={ols_w:.4f}, b={ols_b:.4f}")

# ── Visualization (ERM learning curve / fitted line)
# 1) Learning curve of empirical risk
plt.figure(figsize=(6,4))
plt.plot(history)
plt.xlabel("Epoch")
plt.ylabel("Empirical Risk (MSE)")
plt.title("ERM: Learning Curve (MSE)")
plt.tight_layout()
plt.show()

# 2) Data points and regression lines after training
x_plot = np.linspace(0, 1, 200)
plt.figure(figsize=(6,4))
plt.scatter(x1, y, label="Data")
plt.plot(x_plot, predict(w, b, x_plot), label="ERM (GD)")
plt.plot(x_plot, predict(ols_w, ols_b, x_plot), label="OLS (closed-form)")
plt.xlabel("x"); plt.ylabel("y"); plt.title("Fitted Lines")
plt.legend(); plt.tight_layout(); plt.show()
