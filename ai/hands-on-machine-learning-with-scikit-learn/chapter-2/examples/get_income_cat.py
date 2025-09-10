from get_housing_data import load_housing_data
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedShuffleSplit


if __name__ == "__main__":
    housing = load_housing_data()
    print("Full dataset loaded!")
    print("Rows in full dataset:", len(housing))
    print("First 5 rows of dataset:\n", housing.head())

    # pd.cut() splits a continuous numerical column into discrete categories (bins).
    housing["income_cat"] = pd.cut(housing["median_income"],
                                   bins=[0., 1.5, 3.0, 4.5, 6, np.inf],
                                   labels=[1, 2, 3, 4, 5])
    print("\nFirst 10 rows with income category:\n", housing[["median_income", "income_cat"]].head(10))

    # value_counts() → counts how many rows are in each income category.
    # sort_index() → ensures the categories are in numerical order (1 → 5).
    # .plot.bar() → creates a bar chart of these counts.
    # housing["income_cat"].value_counts().sort_index().plot.bar(rot=0, grid=True)
    # plt.xlabel("Income category")
    # plt.ylabel("Number of districts")
    # plt.show()

    splitter = StratifiedShuffleSplit(n_splits=10, test_size=0.2, random_state=42)
    strat_splits = []
    for train_index, test_index in splitter.split(housing, housing["income_cat"]):
        strat_train_set_n = housing.iloc[train_index]
        strat_test_set_n = housing.iloc[test_index]
        strat_splits.append((strat_train_set_n, strat_test_set_n))

    # Use the first split
    strat_train_set, strat_test_set = strat_splits[0]

    # Shortcut using train_test_split with stratify argument
    strat_train_set, strat_test_set = train_test_split(
        housing, test_size=0.2, stratify=housing["income_cat"], random_state=42
    )

    # Check the income category proportions in the test set
    strat_test_set["income_cat"].value_counts() / len(strat_test_set)

    # Drop the 'income_cat' column to revert data to its original state
    for set_ in (strat_train_set, strat_test_set):
        set_.drop("income_cat", axis=1, inplace=True)