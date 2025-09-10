import numpy as np

def basic_matrix():
    # A x B
    # A(columns) = B(row)


    # Feature matrix (height and weight for 3 people)
    # 3 x 2
    # X => [170, 65]
    #      [180, 75]
    #      [160, 50]
    X = np.array([[170, 65],
                [180, 75],
                [160, 50]])

    print("Feature matrix (X):", X)
    print("Shape of X:", X.shape)

    # Weight vector
    # 2 x 1
    # w => [0.5]
    #      [1.2]
    w = np.array([0.5, 1.2])

    print("Weight vector (w):", w)
    print("Shape of w:", w.shape)

    # Matrix × vector (predicted values)
    y = np.dot(X, w)
    print("Predicted values:", y)
    # Predicted values: [163]
    #                   [180]
    #                   [140]

    # 1 row => 170×0.5+65×1.2=85+78=163
    # 2 row => 180×0.5+75×1.2=90+90=180
    # 3 row => 160×0.5+50×1.2=80+60=140
    # [163, 180, 140]

    # Transpose
    # 2 * 3
    # X.T => [170, 180, 160]
    #        [ 65,  75,  50]
    print("Transpose:\n", X.T)
    print("Shape of X.T:", X.T.shape)


def transpose_matrix():
    # 3 x 2
    # X =>  [170, 65]
    #       [180, 75]
    #       [160, 50]
    X = np.array([[170, 65],
                [180, 75],
                [160, 50]])

    print("Feature matrix (X):", X)
    print("Shape of X:", X.shape)

    # 3 x 1
    # w => [3]
    #      [-2]
    #      [5]
    w = np.array([3, -2, 5])
    print("Weight vector (w):", w)
    print("Shape of w:", w.shape)

    transposed = np.transpose(X)
    y = np.dot(transposed, w)

    print("Transposed matrix (X.T):", transposed)
    print("Result of dot product (y):", y)

    # X.T @ w => [[170, 180, 160],
    #              [ 65,  75,  50]] @ [3, -2, 5]

    # 1 row 170×3 + 180×(−2) + 160×5 = 510−360+800=950
    # 2 row 65×3 + 75×(−2) + 50×5 = 195−150+250=295

def operation():
    # [2, 1]
    # [0, 3]
    # [4, -1]
    x = np.array([[2, 1], [0, 3], [4, -1]])

    # [1]
    # [2]
    w = np.array([1, 2])

    print("x", x.shape)
    print("w", w.shape)

    y = np.dot(x, w)
    print("y", y.shape)

def operation2():
    # [2, 1]
    # [0, 3]
    # [4, -1]
    x = np.array([[2, 1], [0, 3], [4, -1]])

    # [1,2]
    w = np.array([[1, 2]])

    print("x", x.shape)
    print("w", w.shape)

    transposed = np.transpose(w)
    print("Transposed w:", transposed.shape)
    y = np.dot(x, transposed)
    print("y", y.shape)


def identity_inverse_matrix():
    # Identity matrix
    I = np.eye(3)
    print("Identity matrix (I):\n", I)

    # Inverse of the identity matrix
    I_inv = np.linalg.inv(I)
    print("Inverse of identity matrix (I_inv):\n", I_inv)

    result = np.dot(I, I_inv)
    print("I x I_inv:\n", result)

    # A = np.array([1,2], [2,3], [3,4])
    # print("Matrix A:\n", A)


if __name__ == "__main__":
    basic_matrix()
    print("=" * 30)
    transpose_matrix()
    print("=" * 30)
    operation()
    print("=" * 30)
    operation2()
    print("=" * 30)
    identity_inverse_matrix()
