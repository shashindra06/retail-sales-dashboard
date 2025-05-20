import pandas as pd

# Load cleaned data
df = pd.read_csv('online_retail_cleaned.csv')

# Ensure InvoiceDate is datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Basic metrics
total_revenue = df['TotalPrice'].sum()
unique_customers = df['Customer ID'].nunique()
avg_order_value = df.groupby('Invoice')['TotalPrice'].sum().mean()
total_orders = df['Invoice'].nunique()
top_customer = df.groupby('Customer ID')['TotalPrice'].sum().idxmax()
top_customer_revenue = df.groupby('Customer ID')['TotalPrice'].sum().max()

print(f"\nKey Metrics:")
print(f"Total Revenue: £{total_revenue:,.2f}")
print(f"Unique Customers: {unique_customers:,}")
print(f"Average Order Value: £{avg_order_value:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Top Customer ID: {top_customer}, Revenue: £{top_customer_revenue:,.2f}")