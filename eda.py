import pandas as pd

# Load cleaned data
df = pd.read_csv('online_retail_cleaned.csv')

# Ensure InvoiceDate is datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Basic inspection
print("First 5 rows of cleaned dataset:")
print(df.head())
print("\nDataset info:")
print(df.info())
print("\nSummary statistics:")
print(df.describe())