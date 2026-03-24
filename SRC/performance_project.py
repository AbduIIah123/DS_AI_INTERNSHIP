import pandas as pd  #import pandas library for data handling

import matplotlib.pyplot as plt
import seaborn as sns


#load dataset from csv file
df= pd.read_csv("performance.csv")

#drop age column
print(df.isna().sum())
df=df.drop("Age",axis=1)
df.to_csv("data_updated.csv", index=False)
df=df.drop_duplicates()
print(df.shape)

df["Gender"]=df["Gender"].fillna("Unknown")#fill missing values in categorical columns with "unknown"
df = df.dropna(subset=["Student_ID"])
df["Assignment_Score"]=df["Assignment_Score"].fillna(df["Assignment_Score"].median())# Fill missing numerical values with median
df["Internal_Marks"]=df["Internal_Marks"].fillna(df["Internal_Marks"].median())
df["Internet_Access"]=df["Internet_Access"].fillna("Unknown")#Fill missing categorical values with "unknown"

df["Previous_GPA"]=df["Previous_GPA"].fillna(df["Previous_GPA"].mode()[0])#Fill missing values using mode (most frequent value)
df["Attendance"]=df["Attendance"].fillna(df["Attendance"].mode()[0])
df["Study_Hours"]=df["Study_Hours"].fillna(df["Study_Hours"].mode()[0])

print(df)#print cleaned dataset
print(df.shape)#print updated shape after cleaning
df_encoded = pd.get_dummies(df, 
    columns=["Gender","Participation", "Internet_Access", "Family_Background"])#convert categorical columns into numericalusing one hot encoding

df_encoded.to_csv("encoded_student_data.csv", index=False)#save encoded dataset to a new csv file

print(df_encoded.head())#Display first 5 rows of encoded dataset


#Bar plot
sns.set(style="whitegrid")
df.groupby("Gender")["Assignment_Score"].mean().plot(kind="bar")
plt.title("Average Assignment Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Score")
plt.show()

#histogram 
df["Assignment_Score"].plot(kind="hist", bins=10)
plt.title("Distribution of Assignment Scores")
plt.xlabel("Score")
plt.show()

#pie chart
df["Gender"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Gender Distribution")
plt.ylabel("")
plt.show()

# box plot
df["Assignment_Score"].plot(kind="box")
plt.title("Score Spread")
plt.show()

#basline model evaluated
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df_encoded["Final_Result"] = le.fit_transform(df["Final_Result"])

from sklearn.model_selection import train_test_split

X = df_encoded.drop("Final_Result", axis=1)
y = df_encoded["Final_Result"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score

dummy = DummyClassifier(strategy="most_frequent")
dummy.fit(X_train, y_train)

y_dummy = dummy.predict(X_test)

print("Baseline Accuracy:", accuracy_score(y_test, y_dummy))

#logistic regression

print(X_train.dtypes)
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)

y_lr = lr.predict(X_test)

print("Logistic Regression Accuracy:", accuracy_score(y_test, y_lr))

#decision tree
from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(max_depth=5, random_state=42)
dt.fit(X_train, y_train)

y_dt = dt.predict(X_test)

print("Decision Tree Accuracy:", accuracy_score(y_test, y_dt))

#comparing the models
print("\nModel Comparison:")
print("Dummy:", accuracy_score(y_test, y_dummy))
print("Logistic Regression:", accuracy_score(y_test, y_lr))
print("Decision Tree:", accuracy_score(y_test, y_dt))

models = {
    "Dummy": accuracy_score(y_test, y_dummy),
    "Logistic Regression": accuracy_score(y_test, y_lr),
    "Decision Tree": accuracy_score(y_test, y_dt)
    
}

best_model = max(models, key=models.get)

print("Best Model:", best_model)
print("Best Accuracy:", models[best_model])
