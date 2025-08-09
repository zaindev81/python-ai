import numpy as np

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
print("||v1|| =", np.linalg.norm(v1))
print("||v2|| =", np.linalg.norm(v2))

# height, weight
person = np.array([170, 65])
print("person =", person)

# normalization
length = np.linalg.norm(person)
print("length of person =", length)
normalized = person / length
print("normalized person =", normalized)