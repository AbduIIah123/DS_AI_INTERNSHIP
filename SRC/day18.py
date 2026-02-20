# task 1

import pandas as pd 

import sqlite3

conn = sqlite3.connect("C:/Users/abdul/OneDrive/Desktop/database/intern.db")

df = pd.read_sql_query("SELECT name FROM intern WHERE stipend >= 35000;", conn)

df = pd.read_sql_query("SELECT track, avg(stipend) FROM intern GROUP by track;", conn)

df = pd.read_sql_query("SELECT name, COUNT(*) FROM intern GROUP BY name;", conn)
print(df)

#task 2


import pandas as pd 

import sqlite3

conn = sqlite3.connect("C:/Users/abdul/OneDrive/Desktop/database/intern.db")

df = pd.read_sql_query("SELECT intern.name, MENTOR.dept FROM intern INNER JOIN MENTOR ON intern.id = MENTOR.id;", conn)

print(df)