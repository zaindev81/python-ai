from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
from zlib import crc32

def load_housing_data():
    print("Loading housing data...")

    tarball_path = Path("datasets/housing.tgz")
    if not tarball_path.is_file():
        print("Downloading housing data...")
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as housing_tarball: # .extractall(path="datasets"): Extracts all files from the archive into the datasets directory.
            housing_tarball.extractall(path="datasets")

    # Reads the CSV file into a Pandas DataFrame.
    # This makes it easy to analyze and manipulate the data.
    return pd.read_csv(Path("datasets/housing/housing.csv"))


def is_id_in_test_set(identifier, test_ratio):
    return crc32(np.int64(identifier)) < test_ratio * 2**32


def split_data_with_id_hash(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: is_id_in_test_set(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]


def shuffle_and_split_data(data, test_ratio):
    """
    This function randomly shuffles and splits a dataset into training and test sets,
    which is a very common step in machine learning workflows.
    """
    # len(data) → total number of rows in the dataset.
    # np.random.permutation(...) → returns a randomly shuffled array of indices.
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

def main():
    housing = load_housing_data()
    # The info() method is useful to get a quick description of the data, in particular
    # the total number of rows, each attribute’s type, and the number of non-null
    # values:
    print(housing.info())
    print("=" * 60)
    print("housing.describe():")

    # The describe() method shows a summary of the
    # numerical attributes
    print(housing.describe())

    print("=" * 60)
    print("housing.head():")

    print(housing.head())
    print("=" * 60)
    print(housing)
    print("=" * 60)

    # This line of code is counting how many times each unique value appears
    # in the ocean_proximity column of a pandas DataFrame called housing.
    print(housing["ocean_proximity"].value_counts())

    # housing.hist(bins=50, figsize=(12, 8))
    # plt.show()

    train_set, test_set = shuffle_and_split_data(housing, 0.2)
    print(len(train_set), "training samples")
    print(len(test_set), "test samples")


    print("=" * 60)
    housing_with_id = housing.reset_index()  # adds an `index` column
    print(housing_with_id.head())
    train_set, test_set = split_data_with_id_hash(housing_with_id, 0.2, "index")


if __name__ == "__main__":
    main()
