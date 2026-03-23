import pandas as pd  #import pandas library for data handling

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler, MinMaxScaler

#load dataset from csv file
df= pd.read_csv("performance.csv")

#drop age column
print(df.isna().sum())
df=df.drop("Age",axis=1)
df.to_csv("data_updated.csv", index=False)
df=df.drop_duplicates()
print(df.shape)

df["Gender"]=df["Gender"].fillna("Unknown")#fill missing values in categorical columns with "unknown"
df["Student_ID"]=df["Student_ID"].fillna("Unknown")

df["Assignment_Score"]=df["Assignment_Score"].fillna(df["Assignment_Score"].median())#Fill missing numerical values with "unknown"
df["Internal_Marks"]=df["Internal_Marks"].fillna(df["Internal_Marks"].median())
df["Internet_Access"]=df["Internet_Access"].fillna("Unknown")#Fill missing categorical values with "unknown"

df["Previous_GPA"]=df["Previous_GPA"].fillna(df["Previous_GPA"].mode()[0])#Fill missing values using mode (most frequent value)
df["Attendance"]=df["Attendance"].fillna(df["Attendance"].mode()[0])
df["Study_Hours"]=df["Study_Hours"].fillna(df["Study_Hours"].mode()[0])

print(df)#print cleaned dataset
print(df.shape)#print updated shape after cleaning

df_encoded = pd.get_dummies(df, 
                            columns=["Participation", "Internet_Access", 
                                     "Family_Background", "Final_Result"])#convert categorical columns into numericalusing one hot encoding

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
