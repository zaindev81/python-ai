import numpy as np


def basic_operation():
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])

    # vector
    print("v1=", v1)
    print("v2=", v2)

    # add
    print("v1 + v2 =", v1 + v2)

    # subtract
    print("v1 - v2 =", v1 - v2)

    # scalar multiplication
    print("2 * v1 =", 2 * v1)

    # dot product
    print("v1 . v2 =", np.dot(v1, v2))

    # norm
    print("||v1|| =", np.linalg.norm(v1)) # 1, 4, 9
    print("||v2|| =", np.linalg.norm(v2))

    # height, weight
    person = np.array([170, 65])
    print("person =", person)

    # normalization
    length = np.linalg.norm(person)
    print("length of person =", length)
    normalized = person / length
    print("normalized person =", normalized)


def vector_operations():
    v1=  np.array([2, -1, 2])
    v2 = np.array([-1, 4, 0])

    print("add", v1 + v2)
    print("subtract", v1 - v2)
    print("scalar 2 * v", 2 * v1)
    print("dot", v1.dot(v2)) # -2, -4, 0
    print("norm1",np.linalg.norm(v1))
    print("norm2",np.linalg.norm(v2))

    person = np.array([180,60])
    length = np.linalg.norm(person)
    print("normalize", person / length)


if __name__ == "__main__":
    basic_operation()
    print("=" * 30)
    vector_operations()