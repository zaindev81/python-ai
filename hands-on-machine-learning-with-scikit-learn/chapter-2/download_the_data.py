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
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")

    return pd.read_csv(Path("datasets/housing/housing.csv"))


def is_id_in_test_set(identifier, test_ratio):
    return crc32(np.int64(identifier)) < test_ratio * 2**32


def split_data_with_id_hash(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: is_id_in_test_set(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]


def shuffle_and_split_data(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


def main():
    housing = load_housing_data()

    train_set, test_set = shuffle_and_split_data(housing, 0.2)
    print(len(train_set), "training samples")
    print(len(test_set), "test samples")

    print("=" * 60)
    housing_with_id = housing.reset_index()  # adds an `index` column
    print(housing_with_id.head())
    train_set, test_set = split_data_with_id_hash(housing_with_id, 0.2, "index")

    # with_id["id"] = housing["longitude"] * 1000 + housing["latitude"]
    # train_set, test_set = split_data_with_id_hash(housing_with_id, 0.2, "id")

if __name__ == "__main__":
    main()
