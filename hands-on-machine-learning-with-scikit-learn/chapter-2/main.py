from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
import matplotlib.pyplot as plt
import numpy as np

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


def shuffle_and_split_data(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

def main():
    housing = load_housing_data()
    print(housing.info())
    print(housing.head())
    print(housing)
    print(housing["ocean_proximity"].value_counts())

    # housing.hist(bins=50, figsize=(12, 8))
    # plt.show()

    train_set, test_set = shuffle_and_split_data(housing, 0.2)
    print(len(train_set), "training samples")
    print(len(test_set), "test samples")

if __name__ == "__main__":
    main()
