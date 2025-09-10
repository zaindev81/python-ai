import numpy as np
import matplotlib.pyplot as plt

# The prediction error y - ŷ is an array of values.
errors = np.linspace(-5, 5, 200)
print("Errors:", errors)

mse_loss = errors**2            # Mean Squared Error
mae_loss = np.abs(errors)       # Mean Absolute Error

print("MSE Loss:", mse_loss)
print("MAE Loss:", mae_loss)

plt.figure(figsize=(6,4))
plt.plot(errors, mse_loss, label="MSE Loss $(y-\\hat{y})^2$")
plt.plot(errors, mae_loss, label="MAE Loss $|y-\\hat{y}|$")
plt.axvline(0, color="gray", linestyle="--", linewidth=1)
plt.xlabel("Prediction Error (y - ŷ)")
plt.ylabel("Loss")
plt.title("Loss Function Comparison")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()