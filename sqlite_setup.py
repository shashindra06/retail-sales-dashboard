import pandas as pd
import sqlite3

# Load cleaned CSV
df = pd.read_csv('online_retail_cleaned.csv')

# Create SQLite database
conn = sqlite3.connect('retail.db')

# Save DataFrame to SQLite
df.to_sql('sales', conn, if_exists='replace', index=False)

# Verify table creation
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables in database:", cursor.fetchall())

# Quick check: Count rows
cursor.execute("SELECT COUNT(*) FROM sales")
print("Number of rows in sales table:", cursor.fetchone()[0])

# Close connection
conn.close()