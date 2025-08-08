import matplotlib.pyplot as plt

# 1. Prepare data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 2. Create figure (optional) // wide, height
plt.figure(figsize=(6, 4))

# 3. Plot graph
plt.plot(x, y, label="Line")

# 4. Labels, title, etc.
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Basic Plot")
plt.legend() # show label
plt.grid(True)

# 5. Display
plt.show()
