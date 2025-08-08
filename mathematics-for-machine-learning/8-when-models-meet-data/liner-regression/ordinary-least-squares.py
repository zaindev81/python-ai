# ordinary least squares (OLS) method
# least squares method

import numpy as np

def ols(X, y, add_intercept=True):
    """
    Ordinary Least Squares (OLS)
    X: shape (n_samples, n_features)
    y: shape (n_samples,)
    add_intercept: If True, prepend a column of 1s to X (estimate intercept)

    Returns:
      coef: Coefficients (excluding the intercept term)
      intercept: Intercept (0.0 if add_intercept=False)
      y_hat: Predicted values
      rss: Residual sum of squares
      r2: Coefficient of determination (R^2)
    """
    print("X", X)
    print("y", y)

    X = np.asarray(X)
    y = np.asarray(y).reshape(-1)

    print("X", X)
    print("y", y)

    if add_intercept:
        X_design = np.column_stack([np.ones(len(X)), X])  # [1, x1, x2, ...]
    else:
        X_design = X

    # beta = (X^T X)^{-1} X^T y, but use lstsq for numerical stability
    beta, *_ = np.linalg.lstsq(X_design, y, rcond=None)

    if add_intercept:
        intercept = float(beta[0])
        coef = beta[1:]
    else:
        intercept = 0.0
        coef = beta

    y_hat = X_design @ beta
    residuals = y - y_hat
    rss = float(np.sum(residuals ** 2))
    tss = float(np.sum((y - y.mean()) ** 2))
    r2 = 1.0 - (rss / tss)

    return coef, intercept, y_hat, rss, r2

# ===== Example usage (Simple Linear Regression: y = 3x + 2 + noise) =====
if __name__ == "__main__":
    rng = np.random.default_rng(0)
    X = rng.random((100, 1))
    y = 3 * X[:, 0] + 2 + 0.1 * rng.normal(size=100)


    ols(X, y)

    # y = ax + b
