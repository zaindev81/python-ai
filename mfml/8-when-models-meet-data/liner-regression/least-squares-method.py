# ordinary least squares (OLS) method
# least squares method

import numpy as np

def ols(X, y, add_intercept=True):
    return False

# ===== Example usage (Simple Linear Regression: y = 3x + 2 + noise) =====
if __name__ == "__main__":
    rng = np.random.default_rng(0)
    X = rng.random((100, 1))
    y = 3 * X[:, 0] + 2 + 0.1 * rng.normal(size=100)

