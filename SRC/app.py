# ================================
# 1. Import Libraries
# ================================
import streamlit as st
import pickle
import pandas as pd
import os

# ================================
# 2. Load Model & Columns (FIXED PATH ⭐)
# ================================
BASE_DIR = os.path.dirname(__file__)

model = pickle.load(open(os.path.join(BASE_DIR, "..", "model.pkl"), "rb"))
columns = pickle.load(open(os.path.join(BASE_DIR, "..", "columns.pkl"), "rb"))

# ================================
# 3. UI Title
# ================================
st.title("🎓 Student Performance Prediction")

st.write("Enter student details:")

# ================================
# 4. Inputs
# ================================

# Numerical Inputs
assignment_score = st.number_input("Assignment Score", 0.0, 100.0)
internal_marks = st.number_input("Internal Marks", 0.0, 100.0)
previous_gpa = st.number_input("Previous GPA", 0.0, 10.0)
attendance = st.number_input("Attendance (%)", 0.0, 100.0)
study_hours = st.number_input("Study Hours", 0.0, 24.0)

# Categorical Inputs
gender = st.selectbox("Gender", ["Male", "Female", "Unknown"])
participation = st.selectbox("Participation", ["Low", "Medium", "High"])
internet = st.selectbox("Internet Access", ["Yes", "No", "Unknown"])
family = st.selectbox("Family Background", ["Poor", "Average", "Good"])

# ================================
# 5. Prediction Logic
# ================================
if st.button("Predict"):

    input_data = pd.DataFrame([{
        "Assignment_Score": assignment_score,
        "Internal_Marks": internal_marks,
        "Previous_GPA": previous_gpa,
        "Attendance": attendance,
        "Study_Hours": study_hours,
        "Gender": gender,
        "Participation": participation,
        "Internet_Access": internet,
        "Family_Background": family
    }])

    # Encode input
    input_encoded = pd.get_dummies(input_data)

    # Match training columns
    for col in columns:
        if col not in input_encoded:
            input_encoded[col] = 0

    input_encoded = input_encoded[columns]

    # Predict
    prediction = model.predict(input_encoded)[0]

    # Output mapping
    result_map = {
        0: "At Risk",
        1: "Average",
        2: "High Performer"
    }

    st.success(f"Prediction: {result_map.get(prediction)}")
