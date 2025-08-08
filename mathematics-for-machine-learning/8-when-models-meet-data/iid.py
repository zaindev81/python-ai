# independent and identically distributed (i.i.d.)

import numpy as np
import matplotlib.pyplot as plt

# Population data (real world)
np.random.seed(0)
population_size = 100000
X_pop = np.random.uniform(0, 10, size=population_size)
y_pop = 3 * X_pop + 5 + np.random.normal(0, 2, size=population_size)  # True relationship + noise

print("X population:", X_pop)
print("y population:", y_pop)

# Model (simple prediction y = 3x + 5)
def predict(x):
    return 3 * x + 5

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Loss over the entire population
true_risk = mse(y_pop, predict(X_pop))
print("Loss over the entire population:", true_risk)

# --- i.i.d. sample ---
sample_iid_idx = np.random.choice(population_size, size=100, replace=False)
X_iid = X_pop[sample_iid_idx]
y_iid = y_pop[sample_iid_idx]
emp_risk_iid = mse(y_iid, predict(X_iid))
print("Mean loss for i.i.d. sample:", emp_risk_iid)

# --- Non-i.i.d. sample (e.g., x is only in the range 0–2) ---
mask_non_iid = (X_pop >= 0) & (X_pop <= 2)
idx_non_iid = np.random.choice(np.where(mask_non_iid)[0], size=100, replace=False)
X_non_iid = X_pop[idx_non_iid]
y_non_iid = y_pop[idx_non_iid]
emp_risk_non_iid = mse(y_non_iid, predict(X_non_iid))
print("Mean loss for non-i.i.d. sample:", emp_risk_non_iid)

# --- Plot ---
plt.figure(figsize=(8, 4))

# Population (gray histogram)
plt.hist(X_pop, bins=50, alpha=0.3, label="Population (X distribution)", color="gray")

# i.i.d. sample (blue)
plt.scatter(X_iid, y_iid, color="blue", alpha=0.7,
            label=f"i.i.d. sample (Risk={emp_risk_iid:.2f})")

# Non-i.i.d. sample (red)
plt.scatter(X_non_iid, y_non_iid, color="red", alpha=0.7,
            label=f"non-i.i.d. sample (Risk={emp_risk_non_iid:.2f})")

plt.xlabel("X value")
plt.ylabel("y value")
plt.title(f"Population vs Samples (True Risk={true_risk:.2f})")
plt.legend()
plt.tight_layout()
plt.show()
