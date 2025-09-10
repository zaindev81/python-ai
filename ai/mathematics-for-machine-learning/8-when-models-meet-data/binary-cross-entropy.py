import numpy as np
import matplotlib.pyplot as plt

# Predicted probability values from 0.001 to 0.999
# 0 and 1 are avoided because log(0) is undefined.
p = np.linspace(0.001, 0.999, 200)

# True labels
y_true_1 = 1  # Positive class
y_true_0 = 0  # Negative class

# Cross-entropy loss
loss_y1 = -np.log(p)         # when y = 1
loss_y0 = -np.log(1 - p)     # when y = 0

# Plot
plt.figure(figsize=(6,4))
plt.plot(p, loss_y1, label="Loss when y=1")
plt.plot(p, loss_y0, label="Loss when y=0")
plt.xlabel("Predicted Probability")
plt.ylabel("Cross-Entropy Loss")
plt.title("Binary Cross-Entropy Loss")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
