import pandas as pd
import numpy as np

data = pd.DataFrame({
    'Feature': [1, 2, 3, 4, 5],
    'Label': ['A', 'B', 'C', 'D', 'E']
})

def shuffle_and_split_data(data, test_ratio):
    """
    This function randomly shuffles and splits a dataset into training and test sets,
    which is a very common step in machine learning workflows.
    """
    # len(data) → total number of rows in the dataset.
    # np.random.permutation(...) → returns a randomly shuffled array of indices.
    print("Total number of rows in the dataset:", len(data))
    print("Randomly shuffled indices:", np.random.permutation(len(data)))

    shuffled_indices = np.random.permutation(len(data))

    test_set_size = int(len(data) * test_ratio)
    print("Test set size:", test_set_size)

    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]

    # data.iloc[...]
    # .iloc in pandas is integer-location based indexing.
    # It selects rows or columns by their numerical position, not by labels.
    return data.iloc[train_indices], data.iloc[test_indices]


train_set, test_set = shuffle_and_split_data(data, 0.4)

print("Train Set:")
print(train_set)
print("\nTest Set:")
print(test_set)