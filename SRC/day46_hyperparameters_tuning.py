#Project Simulation: Listing Params

from sklearn.tree import DecisionTreeClassifier

# Initialize a default model
model = DecisionTreeClassifier()

# Get all tunable hyperparameters
params = model.get_params()

print("Tunable Hyperparameters for DecisionTreeClassifier:")
for key, value in params.items():
    print(f"{key:20} : {value}")

print("\nKey hyperparameters for complexity:")
print("- max_depth (Tree depth)")
print("- min_samples_split (Minimum samples to split)")

#Project Simulation: Grid Tuning

from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer

# Load data (using breast cancer as a proxy for binary classification)
data = load_breast_cancer()
X, y = data.data, data.target

# Define the grid
param_grid = {
    'max_depth': [2, 4, 6, 8, 10],
    'criterion': ['gini', 'entropy']
}

# Initialize Grid Search
grid = GridSearchCV(
    estimator=DecisionTreeClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring='accuracy'
)

# Fit
grid.fit(X, y)

print(f"Best Parameters: {grid.best_params_}")
print(f"Best CV Accuracy: {grid.best_score_:.4f}")

#Project Simulation: Comparison

from sklearn.model_selection import RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
from scipy.stats import randint

# Load data
data = load_breast_cancer()
X, y = data.data, data.target

# Define distributions
param_dist = {
    'max_depth': randint(2, 20),
    'min_samples_split': randint(2, 20),
    'criterion': ['gini', 'entropy']
}

# Initialize Random Search
random_search = RandomizedSearchCV(
    estimator=DecisionTreeClassifier(random_state=42),
    param_distributions=param_dist,
    n_iter=15, # Only test 15 random combinations
    cv=5,
    scoring='accuracy',
    random_state=42
)

# Fit
random_search.fit(X, y)

print(f"Best Parameters: {random_search.best_params_}")
print(f"Best CV Accuracy: {random_search.best_score_:.4f}")

#Project Simulation: Changing Metrics

from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
X, y = data.data, data.target

param_grid = {'max_depth': [2, 5, 10]}

# Tune for Accuracy
grid_acc = GridSearchCV(DecisionTreeClassifier(), param_grid, scoring='accuracy', cv=3)
grid_acc.fit(X, y)

# Tune for F1
grid_f1 = GridSearchCV(DecisionTreeClassifier(), param_grid, scoring='f1', cv=3)
grid_f1.fit(X, y)

print(f"Best Depth (Accuracy): {grid_acc.best_params_['max_depth']}")
print(f"Best Depth (F1):       {grid_f1.best_params_['max_depth']}")