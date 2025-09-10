# Dimensionality reduction

Let’s explain **the direction of the principal components** using formulas and diagrams.
The essence of PCA is **"finding the direction in which the data spreads the most (maximum variance) and reorienting the coordinate axes along that direction."**

## 1. Direction of the Principal Components (Mathematical Definition)

### (1) Centering by Subtracting the Mean

Given a data matrix $X$ (shape $n \times d$), subtract the mean:

$$
X_{\text{centered}} = X - \bar{X}
$$

This centers the data around the origin.

---

### (2) Construct the Covariance Matrix Representing Variance

$$
\Sigma = \frac{1}{n-1} X_{\text{centered}}^\top X_{\text{centered}}
$$

* $\Sigma$ is the **covariance matrix**
* Each element $\Sigma_{ij}$ represents the correlation between feature $i$ and feature $j$

---

### (3) Eigenvalue Decomposition

$$
\Sigma v = \lambda v
$$

* $v$ → **Eigenvector** (direction of the principal component)
* $\lambda$ → **Eigenvalue** (variance magnitude in that direction)

---

### (4) Selecting the Principal Components

* Sort the eigenvalues in descending order
* Select the top $k$ eigenvectors as the new axes
  (If $k=2$, the data will be reduced to two dimensions)

---

## 2. Why Dimensionality Reduction Can Preserve Information

* Directions with higher variance contain more information
* By keeping the high-variance directions (principal components), the essential structure of the data is mostly preserved
* Directions with small eigenvalues often represent noise or redundant information

---

## 3. Diagram Illustration (Reducing from 2D to 1D)

```
Original Data (2D):
  ●   ●
●       ●
    ●

PCA finds the "maximum variance direction":
   ↘ First Principal Component

Project the data onto that direction (1D):
   •  •    •      •  •
```

→ This way, even in 1D, the data retains the maximum possible variance (information).

---

## 4. Summary

PCA procedure:

1. Subtract the mean (centering)
2. Compute the covariance matrix
3. Perform eigenvalue decomposition
4. Select axes based on largest eigenvalues
5. Project the original data onto those axes to reduce dimensions