# Task 1

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

sns.set(style="whitegrid")

df= pd.read_csv("house-prices.csv")
plt.figure()
sns.histplot(df["Price"],kde=True)
plt.title('Histogram of PRICE')
plt.xlabel('Price')
plt.show()
print("Kurtosis of PRICE",df["Price"].kurt())
print("Skewness of PRICE",df['Price'].skew())
sns.countplot(x='furnishingstatus',data=df)
plt.show()


# Task 2

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

sns.set(style="whitegrid")

df= pd.read_csv("house-prices.csv")
plt.subplot(1, 2, 1)
sns.scatterplot(x='SqFt', y='Price', data=df)
plt.subplot(1, 2, 2)

sns.boxplot(x='Price', y='Brick', data=df)
plt.tight_layout()
plt.show()

print("\nAs X increases, Y seems to increase")

# Task 3


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

sns.set(style="whitegrid")

corr_matrix=df.corr(numeric_only=True)
print(corr_matrix)
sns.heatmap(corr_matrix,annot=True)
plt.show()
sns.boxplot(x=df['price'])
plt.show()