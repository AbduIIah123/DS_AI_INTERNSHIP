import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000

# Generate student IDs
student_ids = [f"STU{str(i).zfill(4)}" for i in range(1, n+1)]

# Generate realistic numerical features
attendance = np.random.normal(75, 15, n).clip(30, 100)
study_hours = np.random.normal(5, 2, n).clip(1, 12)
assignment_score = np.random.normal(70, 15, n).clip(20, 100)
internal_marks = np.random.normal(65, 15, n).clip(20, 100)
previous_gpa = np.random.normal(6.5, 1.5, n).clip(3.0, 10.0)
age = np.random.randint(17, 25, n)

# Generate categorical features
gender = np.random.choice(["Male", "Female"], n, p=[0.5, 0.5])
participation = np.random.choice(["Low", "Medium", "High"], n, p=[0.3, 0.4, 0.3])
internet_access = np.random.choice(["Yes", "No"], n, p=[0.75, 0.25])
family_background = np.random.choice(["Low", "Medium", "High"], n, p=[0.3, 0.4, 0.3])

# Derive Final_Result from actual scores (meaningful labels)
composite = (
    assignment_score * 0.25 +
    internal_marks * 0.25 +
    previous_gpa * 5 +
    attendance * 0.25 +
    study_hours * 2
)

low_thresh = np.percentile(composite, 33)
high_thresh = np.percentile(composite, 67)

def assign_result(score):
    if score <= low_thresh:
        return "At Risk"
    elif score <= high_thresh:
        return "Average"
    else:
        return "High Performer"

final_result = [assign_result(s) for s in composite]

# Build DataFrame
df = pd.DataFrame({
    "Student_ID": student_ids,
    "Age": age,
    "Gender": gender,
    "Attendance": attendance.round(2),
    "Study_Hours": study_hours.round(2),
    "Assignment_Score": assignment_score.round(2),
    "Internal_Marks": internal_marks.round(2),
    "Previous_GPA": previous_gpa.round(2),
    "Participation": participation,
    "Internet_Access": internet_access,
    "Family_Background": family_background,
    "Final_Result": final_result
})

# Save
df.to_csv("performance.csv", index=False)

print("Dataset generated successfully!")
print("Shape:", df.shape)
print("\nFinal_Result distribution:")
print(df["Final_Result"].value_counts())
print("\nSample rows:")
print(df.head())
