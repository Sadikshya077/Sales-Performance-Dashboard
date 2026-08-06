import sqlite3
import pandas as pd

# read cleaned data and store in df
df=pd.read_csv('C:/Users/acer/Desktop/sales project/data/cleaned/Superstore_Cleaned.csv')

conn=sqlite3.connect('database/sales.db')
df.to_sql('sales',conn, if_exists='replace', index=False)

print('Database created successfully')
conn.close()