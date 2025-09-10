### **Simple Linear Regression (one feature x)**

1. **Objective** (minimize the sum of squared residuals)

$$
\min_{a, b} \sum_{i=1}^n \left( y_i - (a x_i + b) \right)^2
$$

2. **Solution (slope $a$ and intercept $b$)**

$$
a = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2}
$$

$$
b = \bar{y} - a \bar{x}
$$

---

### **Multiple Linear Regression (matrix form)**

1. **Objective**

$$
\min_{\boldsymbol{\beta}} \| \mathbf{y} - X \boldsymbol{\beta} \|^2
$$

2. **Solution (normal equation)**

$$
\boldsymbol{\beta} = (X^\mathsf{T} X)^{-1} X^\mathsf{T} \mathbf{y}
$$

* $\boldsymbol{\beta}$ → vector of intercept and coefficients
* $X$ → design matrix (first column is all 1’s for the intercept)
* $\mathbf{y}$ → target variable vector
