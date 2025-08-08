import numpy as np

# np.random
def calc1():
    X = np.random.rand(5,2) # 0 ~ 1
    # matrix
    # [[0.6940679  0.33528883]
    #  [0.81144826 0.55787963]
    #  [0.60840711 0.20159285]
    #  [0.10793578 0.7801112 ]
    #  [0.74381785 0.42332896]]

    print("X", X)
    print("X.shape", X.shape)

    # one-dimensional array
    print(X[:,0]); # [0.74918113 0.944396   0.44864789 0.353366   0.43048044]


def calc2():
    rng = np.random.default_rng(0) # Generator
    X = rng.random((100, 1)) # (100, 1)
    y = rng.normal(size=100) # Generate 100 random numbers from a normal (Gaussian) distribution with a mean of 0 and a standard deviation of 1.
    print(X)
    print(y)

# np.asarray
def calc3():
    print("=" * 30)
    lst = [1,2,3]
    arr = np.asarray(lst)
    print(arr)
    print(type(arr))

    arr_float = np.asarray(lst, dtype=float)
    print(arr_float)

    return False

# np.sum
def calc4():
    print("=" * 30)
    arr = np.array([1, 2, 3])
    total = np.sum(arr)
    print(total)  # 6

    arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
    print(np.sum(arr2))  # 21

    # By column (axis=0)
    print(np.sum(arr2, axis=0))  # [5 7 9]

    # By row (axis=1)
    print(np.sum(arr2, axis=1))  # [ 6 15]

    return False

# np.linalg

calc1()
calc2()
calc3()
calc4()