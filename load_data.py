import pandas as pd


# Load CSV
df = pd.read_csv('online_retail.csv')

# Initial inspection (keep for reference)
print("First 5 rows of the dataset:")
print(df.head())
print("\nDataset information:")
print(df.info())
print("\nSummary statistics for numerical columns:")
print(df.describe())

# Data cleaning
# 1. Remove cancellations (Invoice starting with 'C')
df = df[~df['Invoice'].str.startswith('C', na=False)]

# 2. Drop rows with missing Customer ID
df = df.dropna(subset=['Customer ID'])

# 3. Ensure Quantity and Price are positive
df = df[df['Quantity'] > 0]
df = df[df['Price'] > 0]

# 4. Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# 5. Convert Customer ID to string
df['Customer ID'] = df['Customer ID'].astype(str).str.replace('.0', '', regex=False)

# 6. Add TotalPrice column
df['TotalPrice'] = df['Quantity'] * df['Price']

# 7. Handle missing Description (fill with 'Unknown' for now)
df['Description'] = df['Description'].fillna('Unknown')

# Post-cleaning inspection
print("\nAfter cleaning:")
print("\nFirst 5 rows of cleaned dataset:")
print(df.head())
print("\nCleaned dataset information:")
print(df.info())
print("\nCleaned summary statistics:")
print(df.describe())

# Save cleaned data to CSV (optional, for backup)
df.to_csv('online_retail_cleaned.csv', index=False)
print("\nCleaned data saved to 'online_retail_cleaned.csv'")