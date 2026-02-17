# Task 1

import pandas as pd

data={
      'Name':["A","B","C","D","E","F"],
      'Transmission':['Automatic','Automatic','Manual','Manual','Manual','Automatic'],
      'Color':['Red','Blue','Red','Green','Blue','Green']
      }

df =pd.DataFrame(data)

df['Transmission'] = df['Transmission'].map({'Automatic': 0, 'Manual': 1})

df = pd.get_dummies(df, columns=['Color'], drop_first=True)

print(df)

# Task 2

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler, MinMaxScaler
sns.set(style="whitegrid")

data2={
      'salary':['10000', '20000', '30000'],
      'age':['15', '16', '18']}

d=pd.DataFrame(data2)



scaler1 = StandardScaler()
scaled_features = scaler1.fit_transform(d[['salary', 'age']])
scaler2=MinMaxScaler()
d[['age','salary']]=scaler2.fit_transform(d[['age','salary']])
print("AGE AND SALARY\n",d)

plt.subplot(1,2,1)
plt.title("before scaling")
sns.histplot(d["salary"],kde=True)

plt.subplot(1,2,2)
sns.histplot(scaled_features[:,1],kde=True)
plt.title("after scaling")
plt.show()

#Task 3

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder,MinMaxScaler,StandardScaler,PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

ff=pd.read_csv("gdp.csv")
X_train,X_test,y_train,y_test=train_test_split(ff[['Year']],ff[['Value']],train_size=0.8,random_state=42)
model1=LinearRegression()
model1.fit(X_train,y_train)
baseline_preds=model1.predict(X_test)
baseline_score=r2_score(y_test,baseline_preds)
print("Score when model is trained with original features\n",baseline_score)
poly=PolynomialFeatures(degree=2,include_bias=False)
X_train_poly=poly.fit_transform(X_train)
X_test_poly=poly.transform(X_test)
poly_model=LinearRegression()
poly_model.fit(X_train_poly,y_train)
poly_preds=poly_model.predict(X_test_poly)
poly_score=r2_score(y_test,poly_preds)
print("Score when model is trained with Polynomial Features\n",poly_score)

