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


import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set_style("whitegrid")

# Create output directory for plots
import os
if not os.path.exists('plots'):
    os.makedirs('plots')

# Plot 1: Sales by Country (Top 10)
country_sales = pd.read_csv('sales_by_country.csv')  # Reuse SQL query result
plt.figure(figsize=(10, 6))
sns.barplot(x='Total_Sales', y='Country', data=country_sales.head(10))
plt.title('Top 10 Countries by Sales')
plt.xlabel('Total Sales (£)')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('plots/sales_by_country.png')
plt.close()
print("Saved plot: sales_by_country.png")

# Plot 2: Monthly Sales Trend
monthly_sales = pd.read_csv('monthly_sales.csv')  # Reuse SQL query result
plt.figure(figsize=(12, 6))
sns.lineplot(x='Month', y='Total_Sales', data=monthly_sales, marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales (£)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('plots/monthly_sales.png')
plt.close()
print("Saved plot: monthly_sales.png")

# Plot 3: Top Products by Revenue
top_products = pd.read_csv('top_products.csv')  # Reuse SQL query result
plt.figure(figsize=(10, 6))
sns.barplot(x='Total_Revenue', y='Description', data=top_products)
plt.title('Top 5 Products by Revenue')
plt.xlabel('Total Revenue (£)')
plt.ylabel('Product')
plt.tight_layout()
plt.savefig('plots/top_products.png')
plt.close()
print("Saved plot: top_products.png")

# Plot 4: Distribution of Order Values
order_values = df.groupby('Invoice')['TotalPrice'].sum()
plt.figure(figsize=(10, 6))
sns.histplot(order_values[order_values < 1000], bins=50)
plt.title('Distribution of Order Values (Under £1000)')
plt.xlabel('Order Value (£)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('plots/order_value_distribution.png')
plt.close()
print("Saved plot: order_value_distribution.png")


# Outlier analysis
# High-value orders (top 1%)
order_values = df.groupby('Invoice')['TotalPrice'].sum()
high_value_orders = order_values[order_values > order_values.quantile(0.99)]
print("\nTop 1% Orders by Value ({} orders):".format(len(high_value_orders)))
print(df[df['Invoice'].isin(high_value_orders.index)][['Invoice', 'Customer ID', 'TotalPrice']].drop_duplicates().head())

# Low-price items (bottom 1%)
low_price_items = df[df['Price'] < df['Price'].quantile(0.01)][['Description', 'Price']].drop_duplicates()
print("\nLow-Price Items ({} items):".format(len(low_price_items)))
print(low_price_items.head())