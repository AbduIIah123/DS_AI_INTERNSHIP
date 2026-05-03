# ================================
# 1. Import Libraries
# ================================
import pandas as pd
import numpy as np
import pickle

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# ================================
# 2. Load Dataset
# ================================
df = pd.read_csv("performance.csv")

# ================================
# 3. Data Cleaning
# ================================
if "Age" in df.columns:
    df = df.drop("Age", axis=1)

df = df.drop_duplicates()

df["Gender"] = df["Gender"].fillna("Unknown")
df["Internet_Access"] = df["Internet_Access"].fillna("Unknown")

df["Assignment_Score"] = df["Assignment_Score"].fillna(df["Assignment_Score"].median())
df["Internal_Marks"] = df["Internal_Marks"].fillna(df["Internal_Marks"].median())

df["Previous_GPA"] = df["Previous_GPA"].fillna(df["Previous_GPA"].mode()[0])
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mode()[0])
df["Study_Hours"] = df["Study_Hours"].fillna(df["Study_Hours"].mode()[0])

df = df.dropna(subset=["Student_ID"])

# ================================
# 4. Encoding
# ================================
df_encoded = pd.get_dummies(
    df,
    columns=["Gender", "Participation", "Internet_Access", "Family_Background"],
    drop_first=True
)

le = LabelEncoder()
df_encoded["Final_Result"] = le.fit_transform(df["Final_Result"])

# ================================
# 5. Features & Target
# ================================
X = df_encoded.drop("Final_Result", axis=1)
y = df_encoded["Final_Result"]

# ================================
# 6. Train-Test Split
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ================================
# 7. Scaling (for LR only)
# ================================
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ================================
# 8. Models
# ================================
dummy = DummyClassifier(strategy="most_frequent")
lr = LogisticRegression(max_iter=1000)
dt = DecisionTreeClassifier(max_depth=5, random_state=42)
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# ================================
# 9. Cross Validation
# ================================
print("\nCross Validation Scores:")
print("Dummy:", cross_val_score(dummy, X_train, y_train, cv=5).mean())
print("Logistic Regression:", cross_val_score(lr, X_train_scaled, y_train, cv=5).mean())
print("Decision Tree:", cross_val_score(dt, X_train, y_train, cv=5).mean())
print("Random Forest:", cross_val_score(rf, X_train, y_train, cv=5).mean())

# ================================
# 10. Train Models
# ================================
dummy.fit(X_train, y_train)
lr.fit(X_train_scaled, y_train)
dt.fit(X_train, y_train)
rf.fit(X_train, y_train)

# ================================
# 11. Predictions
# ================================
y_dummy = dummy.predict(X_test)
y_lr = lr.predict(X_test_scaled)
y_dt = dt.predict(X_test)
y_rf = rf.predict(X_test)

# ================================
# 12. Accuracy
# ================================
dummy_acc = accuracy_score(y_test, y_dummy)
lr_acc = accuracy_score(y_test, y_lr)
dt_acc = accuracy_score(y_test, y_dt)
rf_acc = accuracy_score(y_test, y_rf)

print("\nTest Accuracy:")
print("Dummy:", dummy_acc)
print("Logistic Regression:", lr_acc)
print("Decision Tree:", dt_acc)
print("Random Forest:", rf_acc)

# ================================
# 13. Evaluation (RF)
# ================================
print("\nClassification Report (Random Forest):")
print(classification_report(y_test, y_rf))

# ================================
# 14. Best Model Selection
# ================================
models = {
    "Dummy": dummy_acc,
    "Logistic Regression": lr_acc,
    "Decision Tree": dt_acc,
    "Random Forest": rf_acc
}

best_model = max(models, key=models.get)

print("\nBest Model:", best_model)
print("Best Accuracy:", models[best_model])

# ================================
# 15. SAVE MODEL (IMPORTANT ⭐)
# ================================
pickle.dump(rf, open("model.pkl", "wb"))
pickle.dump(X.columns.tolist(), open("columns.pkl", "wb"))

print("\nModel and columns saved successfully!")