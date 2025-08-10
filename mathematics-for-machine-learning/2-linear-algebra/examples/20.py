# 20

import numpy as np

# Ax = b

# Coefficient matrix A (a_ij)
# [2, 1, 3]
# [1, 2, 1]
# [3, 2, 2]
A = np.array([
    [2, 1, 3],  # Amounts of N1, N2, N3 required for resource R1
    [1, 2, 1],  # Resource R2
    [3, 2, 2]   # Resource R3
])

# Resource stock vector b
# [10]
# [8]
# [13]
b = np.array([10, 8, 13])


# Solve the system of linear equations A x = b
# 2*x1 + 1*x2 + 3*x3 = 10
# 1*x1 + 2*x2 + 1*x3 = 8
# 3*x1 + 2*x2 + 2*x3 = 13
x = np.linalg.solve(A, b)

print("Solution x =", x)
