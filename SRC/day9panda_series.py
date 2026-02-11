#task 1

import pandas as pd 

products=pd.Series([700,150,300], index=('Laptop', 'Mouse', 'Keyboard'))

print(products['Laptop'])

print(products[['Laptop', 'Mouse']])

products[1:2]

#task 2

import pandas as pd 

grades=pd.Series([85, None, 92, 45, None, 78, 55])

print(grades.isnull())

print(grades.fillna(0))

passed=grades[grades>60]

print(passed)

#task3

import pandas as pd 

usernames=pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

print(usernames)

print(usernames.str.lower())

print(usernames.str.strip())

print(usernames.str.contains('a'))
