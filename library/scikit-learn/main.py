from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

"""
This Python code is a simple machine learning workflow using scikit-learn.
It trains and evaluates a Random Forest model on the Iris dataset,
which is a classic dataset for classification. Here's a step-by-step explanation:
"""

# Load dataset
# iris.data (X): Input features (flower measurements: sepal length, sepal width, petal length, petal width).
# iris.target (y): Labels (flower species: Setosa, Versicolor, Virginica).

iris = load_iris()
X, y = iris.data, iris.target

# Split into train and test sets
# 80% training data, 20% testing data (test_size=0.2).
# random_state=42 ensures reproducible results.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model
# RandomForestClassifier: Machine learning model that uses multiple decision trees (an ensemble method).
# Random Forest works by creating many decision trees and combining their results to improve accuracy and reduce overfitting.
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
# accuracy_score: Evaluates how well the model performs.
print("Accuracy:", accuracy_score(y_test, y_pred))