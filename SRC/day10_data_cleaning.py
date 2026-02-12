#Task 1

import pandas as pd
df= pd.read_csv("customer_orders.csv")
print((df.duplicated().sum()))
print(df.isna().sum())
df=df.drop_duplicate()

df["name"]=df["name"].fillna("unknown")
df["price"]=df["price"].fillna(df["price"].median())
df["payment_mode"]=df["payment_mode"].fillna(df["payment_mode"].mode()[0])
df["location"]=df["location"].fillna(df["location"].mode()[0])
df["customer_ID"]=df["customer_ID"].fillna(0)

print(df)
print(df.shape)

#Task 2

data=pd.read_csv("customer_orders.csv")
print(data.dtypes)

data["price"]=data["price"].str.replace("$","")
print(data)
print(data["price"].astype(float))
pd.to_datetime(data["date"])

#Task 3

d=pd.read_csv("customer_orders.csv")
d["location"]=d["location"].str.strip()
d["location"]=d["location"].str.lower()
unique=d["location"].unique()
print(unique)
