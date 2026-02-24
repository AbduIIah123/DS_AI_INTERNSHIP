import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

sns.set(style="whitegrid")

df= pd.read_csv("customer_analytics.csv")

#setup and inspection

df.head()
df.info()
df.describe()
df.shape
df.tail()
print("The dataset represents 205 customer data with features such as age, annual income, purchase amount, prefered devices, etc")
df.to_csv('cleaned_customer_analytics.csv',index=False)

#data preprocessing

print((df.duplicated().sum()))
print(df.isna().sum())
df=df.drop_duplicates()
print(df.duplicated().sum())
df["Education"]=df["Education"].fillna("unknown")
df["AnnualIncome"]=df["AnnualIncome"].fillna(df["AnnualIncome"].mean())
print("Education and annual income columns contained missing values.\nEducation column was dropped as it did not have much significance in our analysis.\nAnnual income missing values where filled using their mean, ie., 74499.90")

#histogram of annual income

plt.figure()
sns.histplot(df["AnnualIncome"])
plt.title('Histogram of AnnualIncome')
plt.show()
plt.xlabel('AnnualIncome')
sns.plot(x='AnnualIncome',data=df)
plt.show()


#histogram of spending score

plt.figure()
sns.histplot(df["SpendingScore"])
plt.title('Histogram of SpendingScore')
plt.show()
plt.xlabel('SpendingScore')
sns.plot(x='SpendingScore',data=df)
plt.show()

#count plot

sns.countplot(x='Gender',data=df)
plt.show()

#box plot

sns.boxplot(x=df["MaritalStatus"],y=df["LastPurchaseAmount"])
plt.title("Marital Status vs Purchase Amount boxplot.\nSingles purchase amount is higher on average than married")
plt.show()

#scatter plot

plt.scatter(x='Age',y='YearsEmployed', data=df)
plt.show()

#correlation matrix

corr_matrix=df.corr(numeric_only=True)
print(corr_matrix)
sns.heatmap(corr_matrix,annot=True)
plt.show()
print("3. Most features provided do not have high correlation at all, except age and years employed, having a strong positive correlation 0f 0.97")