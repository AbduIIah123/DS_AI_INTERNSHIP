# Import Libraries
import streamlit as st
import pickle
import pandas as pd
import os

# Load Model & Columns
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(BASE_DIR, "..")
model = pickle.load(open(os.path.join(ROOT_DIR, "model.pkl"), "rb"))
columns = pickle.load(open(os.path.join(ROOT_DIR, "columns.pkl"), "rb"))

# UI Title
st.title("Student Performance Prediction")
st.write("Enter student details:")

# Numerical Inputs
assignment_score = st.number_input("Assignment Score", 0.0, 100.0)
internal_marks = st.number_input("Internal Marks", 0.0, 100.0)
previous_gpa = st.number_input("Previous GPA", 0.0, 10.0)
attendance = st.number_input("Attendance (%)", 0.0, 100.0)
study_hours = st.number_input("Study Hours", 0.0, 24.0)

# Categorical Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
participation = st.selectbox("Participation", ["Low", "Medium", "High"])
internet = st.selectbox("Internet Access", ["Yes", "No"])
family = st.selectbox("Family Background", ["Low", "Medium", "High"])

# Prediction Logic
if st.button("Predict"):
    input_encoded = pd.DataFrame([{col: 0 for col in columns}])

    num_map = {
        "Assignment_Score": assignment_score,
        "Internal_Marks": internal_marks,
        "Previous_GPA": previous_gpa,
        "Attendance": attendance,
        "Study_Hours": study_hours,
    }
    for col, val in num_map.items():
        if col in input_encoded.columns:
            input_encoded[col] = val

    cat_map = {
        "Gender": gender,
        "Participation": participation,
        "Internet_Access": internet,
        "Family_Background": family,
    }
    for feature, value in cat_map.items():
        col_name = f"{feature}_{value}"
        if col_name in input_encoded.columns:
            input_encoded[col_name] = 1

    input_encoded = input_encoded[columns]

    prediction = model.predict(input_encoded)[0]

    result_map = {
        0: "At Risk",
        1: "Average",
        2: "High Performer"
    }

    st.success(f"Prediction: {result_map.get(prediction, 'Unknown')}")