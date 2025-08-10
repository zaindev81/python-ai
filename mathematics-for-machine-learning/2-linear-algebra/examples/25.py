import numpy as np

# Prepare matrices with compatible shapes
A = np.array([[1, 2, 0],
              [0, 1, 3]], dtype=float)          # (2x3)
B = np.array([[2, -1, 4, 0],
              [1,  3, 0, 5],
              [2,  2, 1, 1]], dtype=float)      # (3x4)
C = np.array([[1, 0],
              [2, 1],
              [0, 3],
              [4, 2]], dtype=float)             # (4x2)

# Associative Law (AB)C = A(BC)
lhs_assoc = (A @ B) @ C # (2x3) x (3x4) = (2x4) -> (2x4) x (4x2) = (2x2)
rhs_assoc = A @ (B @ C)
print("Left-hand side (AB)C:\n", lhs_assoc)
print("Right-hand side A(BC):\n", rhs_assoc)
print("Associativity holds?:", np.allclose(lhs_assoc, rhs_assoc))

# equal
# lhs = np.dot(np.dot(A, B), C)  # (2x4) x (4x2) = (2x2)
# print("Left-hand side (AB)C:\n", lhs)

# Distributive Law (A + A)B = AB + AB
lhs_dist = (A + A) @ B
rhs_dist = (A @ B) + (A @ B)
print("Left-hand side (A + A)B:\n", lhs_dist)
print("Right-hand side AB + AB:\n", rhs_dist)
print("Distributivity holds?:", np.allclose(lhs_dist, rhs_dist))

# Identity Matrix
# I_m A = A, A I_n = A
Im = np.eye(A.shape[0])   # (2x2)
In = np.eye(A.shape[1])   # (3x3)
print("Left identity holds?:", np.allclose(Im @ A, A))
print("Right identity holds?:", np.allclose(A @ In, A))

# Transpose with Scalar (λC)^T = C^T λ
lam = 2.5
check_transpose_scalar = np.allclose(((lam * C).T), (C.T * lam))
print("Transpose-scalar move holds?:", check_transpose_scalar)

# --- 2) Inverse of a 2x2 matrix (Eq. 2.24) -----------------------------------
def inv2x2(M):
    """Return the inverse of a 2x2 matrix using Eq. (2.24) if it exists.
       If it does not exist, return None."""
    a11, a12 = M[0, 0], M[0, 1]
    a21, a22 = M[1, 0], M[1, 1]
    det = a11 * a22 - a12 * a21
    if np.isclose(det, 0.0):
        return None
    return (1.0 / det) * np.array([[ a22, -a12],
                                   [-a21,  a11]], dtype=float)

A2 = np.array([[3, 1],
               [4, 2]], dtype=float)
A2_inv = inv2x2(A2)
print("A2 inverse:\n", A2_inv)
if A2_inv is not None:
    print("A2 * A2_inv ≈ I?:", np.allclose(A2 @ A2_inv, np.eye(2)))
    print("A2_inv * A2 ≈ I?:", np.allclose(A2_inv @ A2, np.eye(2)))

# --- 3) Solve the system of linear equations (2.35) represented as A x = b
#       (solution given by Eq. 2.36) -------------------------------------------
A_sys = np.array([[ 2,  3,  5],
                  [ 4, -2, -7],
                  [ 9,  5, -3]], dtype=float)
b_sys = np.array([1, 8, 2], dtype=float)

# Solve (unique solution if A is nonsingular)
x = np.linalg.solve(A_sys, b_sys)
print("Solution x (x1, x2, x3):", x)

# Verification: Is A x ≈ b ?
print("Check A x ≈ b?:", np.allclose(A_sys @ x, b_sys))

# View as a linear combination of columns of A
# (superimposing A's column vectors with x1, x2, x3)
col1, col2, col3 = A_sys[:, 0], A_sys[:, 1], A_sys[:, 2]
lincomb = x[0] * col1 + x[1] * col2 + x[2] * col3
print("Linear combination equals b?:", np.allclose(lincomb, b_sys))