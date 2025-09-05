from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
import numpy as np

def fetch_mnist_data():
    print("Fetching MNIST data...")
    mnist = fetch_openml("mnist_784", version=1, as_frame=False)  # Load MNIST
    return mnist

def plot_digit(image_data):
    image = image_data.reshape(28, 28)
    plt.imshow(image, cmap="binary")    # Display grayscale image
    plt.axis("off")                     # Hide axes

def main():
    print("Hello from chapter-3!")

    # Fetch the MNIST dataset
    mnist = fetch_mnist_data()

    # Show dictionary keys of MNIST dataset
    print(mnist.keys())

    # Separate features and labels
    X, y = mnist.data, mnist.target
    print("X shape:", X.shape)  # (70000, 784)
    print("y shape:", y.shape)  # (70000,)

    # Convert target to integer type
    y = y.astype(np.uint8)

    # Display the first digit
    some_digit = X[0]
    plot_digit(some_digit)
    plt.show()

if __name__ == "__main__":
    main()
