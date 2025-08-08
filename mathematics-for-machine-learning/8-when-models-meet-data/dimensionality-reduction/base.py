from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

"""
Dimensional Reduction (Dimensionality Reduction)
Purpose: Compress features while preserving information.
Exercise: Reduce to two dimensions using PCA and visualize.
"""

X, y = load_iris(return_X_y=True)
pca = PCA(n_components=2) # reduce to 2D
X_pca = pca.fit_transform(X) # fit -> transform

print("X", X) # Feature
print("y", y) # label
print("pca", pca) # PCA
print("X_pca", X_pca) # PCA transformed

plt.scatter(X_pca[:,0], X_pca[:,1], c=y)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Iris Dataset')
plt.colorbar()
plt.show()

# plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y)
# plt.show()