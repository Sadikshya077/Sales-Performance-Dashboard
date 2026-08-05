import pandas as pd

# Read the dataset
#dataset path = C:/Users/acer/Desktop/sales project/data/raw/Superstore.csv

df = pd.read_csv("C:/Users/acer/Desktop/sales project/data/raw/Superstore.csv", encoding="latin1")

# Display the first 5 rows
print("\nFirst 5 Rows:")
print(df.head()) # print is needed as it just returns value without printing it.

# Number of rows and columns
print("\nShape of the dataset:")
print(df.shape) 

# Column names
print("\nColumns:")
print(df.columns)

# Data types and missing values
print("\nDataset Information:")
df.info() # print is not needed as it displays the information directly and returns None.

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print(df.dtypes)

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("\nUpdated Data Types:")
df.info()

# Create Year and Month columns
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month_name()

# Create Shipping Days
df["Shipping Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

# Create Profit Margin (%)
df["Profit Margin"] = (df["Profit"] / df["Sales"]) * 100

print(df[["Year", "Month"]].head())

df.to_csv("C:/Users/acer/Desktop/sales project/data/cleaned/Superstore_Cleaned.csv", index=False)