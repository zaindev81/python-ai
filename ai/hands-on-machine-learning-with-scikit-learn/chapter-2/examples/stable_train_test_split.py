from get_housing_data import load_housing_data
from zlib import crc32
from sklearn.model_selection import train_test_split
import numpy as np


"""
CRC32 is a hash function that converts data (like an ID) into a fixed-size integer.
→ It’s used here to generate stable and repeatable "randomness".
"""


def is_id_in_test_set(identifier, test_ratio):
    """Decides whether a data point should go into the test set or not."""
    id = np.int64(identifier)
    crc = crc32(id)

    # print("id", id, "→ crc32:", crc)
    # print("test_ratio * 2**32:", test_ratio * 2**32)
    # test_ratio * 2**32: 858993459.2

    return crc32(np.int64(identifier)) < test_ratio * 2**32


def split_data_with_id_hash(data, test_ratio, id_column):
    ids = data[id_column]
    # print("IDs for splitting:", ids)
    in_test_set = ids.apply(lambda id_: is_id_in_test_set(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set] # False, True


if __name__ == "__main__":
    housing = load_housing_data()
    print("Full dataset loaded!")
    print("Rows in full dataset:", len(housing))
    print("First 5 rows of dataset:\n", housing.head())

    # ==============================================================
    # 1. Use Row Index as ID
    # ==============================================================
    print("\n=== METHOD 1: Using row index as ID ===")
    housing_with_id = housing.reset_index()  # Add an `index` column
    train_set, test_set = split_data_with_id_hash(housing_with_id, 0.2, "index")

    print("\n[RESULT: INDEX METHOD]")
    print("Train size:", len(train_set))
    print("Test size :", len(test_set))
    print("Test ratio:", len(test_set) / len(housing))

    # ==============================================================
    # 2. Geo ID (longitude * 1000 + latitude)
    # ==============================================================
    print("\n=== METHOD 2: Using GEO ID (longitude * 1000 + latitude) ===")
    housing_with_geo_id = housing.copy()
    housing_with_geo_id["geo_id"] = housing["longitude"] * 1000 + housing["latitude"]

    # Debug: Check geo_id values
    print("First 10 geo_id values:\n", housing_with_geo_id["geo_id"].head(10))

    train_set, test_set = split_data_with_id_hash(housing_with_geo_id, 0.2, "geo_id")

    print("\n[RESULT: GEO ID METHOD]")
    print("Train size:", len(train_set))
    print("Test size :", len(test_set))
    print("Test ratio:", len(test_set) / len(housing))

    # ==============================================================
    # 3. sklearn's train_test_split
    # ==============================================================
    print("\n=== METHOD 3: Using sklearn train_test_split ===")
    train_set, test_set = train_test_split(housing.copy(), test_size=0.2, random_state=42)

    print("\n[RESULT: SKLEARN METHOD]")
    print("Train size:", len(train_set))
    print("Test size :", len(test_set))
    print("Test ratio:", len(test_set) / len(housing))

    # ==============================================================
    # Final check: Display the first few rows of the test set
    # ==============================================================
    print("\n=== Final Test Set Preview ===")
    print(test_set.head())
