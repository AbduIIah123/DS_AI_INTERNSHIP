#Euclidean & Manhattan

import numpy as np

point1 = np.array([2, 3])
point2 = np.array([5, 7])

# Euclidean Distance
euclidean = np.linalg.norm(point1 - point2)

# Manhattan Distance
manhattan = np.sum(np.abs(point1 - point2))

print(f"Point 1: {point1}")
print(f"Point 2: {point2}")
print(f"Euclidean: {euclidean:.4f}")
print(f"Manhattan: {manhattan}")

#Testing K-Values

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load dataset
X, y = load_iris(return_X_y=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Test k = 1, 3, 5, 15
for k in [1, 3, 5, 15]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    accuracy = knn.score(X_test, y_test)
    print(f"k = {k:2d} | Accuracy: {accuracy:.4f}")
    
#Full KNN Implementation
    
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

# Load data
X, y = load_iris(return_X_y=True)

# 1. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 2. Initialize model
knn = KNeighborsClassifier(n_neighbors=5)

# 3. Fit model
knn.fit(X_train, y_train)

# 4. Predict
predictions = knn.predict(X_test)

# 5. Evaluate
acc = accuracy_score(y_test, predictions)
print(f"Final Accuracy: {acc:.4f}")
print(f"First 5 predictions: {predictions[:5]}")
print(f"First 5 actual labels: {y_test[:5]}")





