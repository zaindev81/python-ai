from get_housing_data import load_housing_data
from zlib import crc32
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

    # Since the housing dataset does not have an identifier column,
    # use the row index as the ID:
    housing_with_id = housing.reset_index()  # adds an `index` column
    train_set, test_set = split_data_with_id_hash(housing_with_id, 0.2, "index")

    print("Rows in full dataset:", len(housing))
    print("Rows in train set:", len(train_set))
    print("Rows in test set:", len(test_set))
    print("\nTest set proportion:", len(test_set) / len(housing))
    print("\nFirst 5 rows of the test set:")
    print(test_set.head())