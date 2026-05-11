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
st.title("🎓 Student Performance Prediction")
st.write("Enter student details:")

# Numerical Inputs
assignment_score = st.number_input("Assignment Score", 0.0, 100.0)
internal_marks = st.number_input("Internal Marks", 0.0, 100.0)
previous_gpa = st.number_input("Previous GPA", 0.0, 10.0)
attendance = st.number_input("Attendance (%)", 0.0, 100.0)
study_hours = st.number_input("Study Hours", 0.0, 24.0)

# Categorical Inputs
gender = st.selectbox("Gender", ["Male", "Female", "Unknown"])
participation = st.selectbox("Participation", ["Low", "Medium", "High"])
internet = st.selectbox("Internet Access", ["Yes", "No"])
family = st.selectbox("Family Background", ["Low", "Medium", "High"])

# Prediction Logic
if st.button("Predict"):

    # Start with all expected columns set to 0
    input_encoded = pd.DataFrame([{col: 0 for col in columns}])

    # Fill numerical columns
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

    # Fill one-hot encoded categorical columns
    cat_map = {
        "Gender": gender,
        "Participation": participation,
        "Internet_Access": internet,
        "Family_Background": family,
    }