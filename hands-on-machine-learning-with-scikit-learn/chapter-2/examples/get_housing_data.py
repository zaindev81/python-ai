from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
import matplotlib.pyplot as plt


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


if __name__ == "__main__":
    housing = load_housing_data()
    # The info() method is useful to get a quick description of the data, in particular
    # the total number of rows, each attribute’s type, and the number of non-null
    # values:


    # The info() method is useful to get a quick description of the data, in particular
    # the total number of rows, each attribute’s type, and the number of non-null
    #
    # Shows:
    # - Total rows
    # - Column names and data types
    # - Non-null value counts
    # - Memory usage
    print("=" * 60)
    print("housing.info():")
    print("=" * 60)
    print(housing.info())


    # The describe() method shows a summary of the numerical attributes
    #
    # Shows statistical details for numeric columns:
    #   Count, mean, std, min, max, and quartiles (25%, 50%, 75%).
    print("=" * 60)
    print("housing.describe():")
    print("=" * 60)
    print(housing.describe())


    # Displays the first 5 rows of the dataset.
    # Helps quickly check what the data looks like.
    print("=" * 60)
    print("housing.head():")
    print("=" * 60)
    print(housing.head())


    # This line of code is counting how many times each unique value appears
    # in the ocean_proximity column of a pandas DataFrame called housing.
    print("=" * 60)
    print("housing['ocean_proximity']:")
    print(housing["ocean_proximity"].value_counts())


    # adds an `index` column
    print("=" * 60)
    print("housing.reset_index:")
    print("=" * 60)
    housing_with_id = housing.reset_index()  # adds an `index` column
    print(housing_with_id.head())

    """
    You can either plot this one attribute at a time, or you can
    call the hist() method on the whole dataset (as shown in the following code
    example), and it will plot a histogram for each numerical attribute (see
    """
    # print("=" * 60)
    # print("housing.hist:")
    # print("=" * 60)
    # housing.hist(bins=50, figsize=(12, 8))
    # plt.show()
