# ================================
# IMPORT LIBRARIES
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
# LOAD DATASET
# ================================
df = pd.read_csv("performance.csv")

# ================================
# DATA CLEANING
# ================================
if "Age" in df.columns:
    df = df.drop("Age", axis=1)
if "Student_ID" in df.columns:
    df = df.drop("Student_ID", axis=1)

df = df.drop_duplicates()

df["Gender"] = df["Gender"].fillna("Unknown")
df["Internet_Access"] = df["Internet_Access"].fillna("No")
df["Assignment_Score"] = df["Assignment_Score"].fillna(df["Assignment_Score"].median())
df["Internal_Marks"] = df["Internal_Marks"].fillna(df["Internal_Marks"].median())
df["Previous_GPA"] = df["Previous_GPA"].fillna(df["Previous_GPA"].mode()[0])
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mode()[0])
df["Study_Hours"] = df["Study_Hours"].fillna(df["Study_Hours"].mode()[0])

# ================================
# FIX FINAL_RESULT LABELS
# ================================
df["composite"] = (
    df["Assignment_Score"] * 0.25 +
    df["Internal_Marks"] * 0.25 +
    df["Previous_GPA"] * 5 +
    df["Attendance"] * 0.25 +
    df["Study_Hours"] * 2
)

low_thresh = df["composite"].quantile(0.33)
high_thresh = df["composite"].quantile(0.67)

def assign_result(score):
    if score <= low_thresh:
        return "At Risk"
    elif score <= high_thresh:
        return "Average"
    else:
        return "High Performer"

df["Final_Result"] = df["composite"].apply(assign_result)
df = df.drop("composite", axis=1)

print("Final_Result distribution:")
print(df["Final_Result"].value_counts())

# ================================
# ENCODING
# ================================
df_encoded = pd.get_dummies(
    df,
    columns=["Gender", "Participation", "Internet_Access", "Family_Background"],
    drop_first=False
)

df_encoded = df_encoded.astype(
    {col: int for col in df_encoded.select_dtypes(include="bool").columns}
)

# ================================
# LABEL ENCODING TARGET
# ================================
le = LabelEncoder()
df_encoded["Final_Result"] = le.fit_transform(df["Final_Result"])
print("\nLabel classes (0,1,2):", le.classes_)

pickle.dump(le, open("label_encoder.pkl", "wb"))

# ================================
# FEATURES & TARGET
# ================================
X = df_encoded.drop("Final_Result", axis=1)
y = df_encoded["Final_Result"]

print("\nTraining columns:", X.columns.tolist())

# ================================
# SAVE COLUMNS
# ================================
pickle.dump(X.columns.tolist(), open("columns.pkl", "wb"))

# ================================
# TRAIN TEST SPLIT
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ================================
# FEATURE SCALING
# ================================
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
pickle.dump(scaler, open("scaler.pkl", "wb"))

# ================================
# MODELS
# ================================
dummy = DummyClassifier(strategy="most_frequent")
lr = LogisticRegression(max_iter=2000)
dt = DecisionTreeClassifier(max_depth=5, random_state=42)
rf = RandomForestClassifier(
    n_estimators=500,
    max_depth=15,
    min_samples_split=4,
    class_weight="balanced_subsample",
    random_state=42
)

# ================================
# CROSS VALIDATION
# ================================
print("\nCross Validation Scores:")
print("Dummy:", cross_val_score(dummy, X_train, y_train, cv=5).mean())
print("Logistic Regression:", cross_val_score(lr, X_train_scaled, y_train, cv=5).mean())
print("Decision Tree:", cross_val_score(dt, X_train, y_train, cv=5).mean())
print("Random Forest:", cross_val_score(rf, X_train, y_train, cv=5).mean())

# ================================
# TRAIN MODELS
# ================================
dummy.fit(X_train, y_train)
lr.fit(X_train_scaled, y_train)
dt.fit(X_train, y_train)
rf.fit(X_train, y_train)

# ================================
# PREDICTIONS
# ================================
y_dummy = dummy.predict(X_test)
y_lr = lr.predict(X_test_scaled)
y_dt = dt.predict(X_test)
y_rf = rf.predict(X_test)

# ================================
# ACCURACY
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

print("\nClassification Report (Random Forest):")
print(classification_report(y_test, y_rf, target_names=le.classes_))

# ================================
# BEST MODEL & SAVE
# ================================
model_objects = {
    "Dummy": (dummy, dummy_acc),
    "Logistic Regression": (lr, lr_acc),
    "Decision Tree": (dt, dt_acc),
    "Random Forest": (rf, rf_acc)
}

best_name = max(model_objects, key=lambda k: model_objects[k][1])
best_model_obj = model_objects[best_name][0]

print("\nBest Model:", best_name)
print("Best Accuracy:", model_objects[best_name][1])

pickle.dump(best_model_obj, open("model.pkl", "wb"))
print("\nmodel.pkl saved successfully!")
print("columns.pkl saved successfully!")
print("label_encoder.pkl saved successfully!")
print("scaler.pkl saved successfully!")