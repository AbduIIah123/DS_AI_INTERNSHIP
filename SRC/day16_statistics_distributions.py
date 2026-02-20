#Task 1: The Shape Shifter (Visualizing Distributions)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
        "heights" : [172,166,162,185,158,167,163,170,168,166],
        "income" : [60000,42000,95000,37000,80000,110000,65000,55000,45000,42000],
        "test" : [40,78,68,89,87,62,94,95,57,79]
        }

df = pd.DataFrame(data)

plt.figure()
sns.histplot(df["heights"],kde=True)
plt.title("Normal data")
plt.show()

plt.figure()
sns.histplot(df["income"],kde=True)
plt.title("Right-skewed data")
plt.show()

plt.figure()
sns.histplot(df["test"],kde=True)
plt.title("Left-skewed data")
plt.show()


print("Normal mean: ",df["heights"].mean())
print("Normal median: ",df["heights"].median())
print("Right-skewed mean: ",df["income"].mean())
print("Right-skewed median: ",df["income"].median())
print("Left-skewed mean: ",df["test"].mean())
print("Left-skewed median: ",df["test"].median())



#Task 2: The Outlier Detective (Z-Scores)
mean = df["heights"].mean()
std = df["heights"].std()
df["z-score"]=(df["heights"]-mean)/std
outliers=df[np.abs(df["z-score"])>2]
print(outliers)



#Task 3: The Magic of Averages (Central Limit Theorem)
sample_means=[]
for i in range (1000):
    sample=np.random.choice(df["income"],size=30)
    sample_means.append(sample.mean())
    
plt.figure()
sns.histplot(sample_means,kde=True)
plt.title("Right-skewed data after CLT")
plt.show()