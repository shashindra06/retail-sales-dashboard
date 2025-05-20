import pandas as pd

# Load data
df = pd.read_csv('online_retail_cleaned.csv')
country_sales = pd.read_csv('sales_by_country.csv')
top_products = pd.read_csv('top_products.csv')
monthly_sales = pd.read_csv('monthly_sales.csv')
top_customers = pd.read_csv('top_customers.csv')

# Calculate metrics
total_revenue = df['TotalPrice'].sum()
unique_customers = df['Customer ID'].nunique()
avg_order_value = df.groupby('Invoice')['TotalPrice'].sum().mean()
total_orders = df['Invoice'].nunique()
top_customer_id = top_customers.iloc[0]['Customer ID']
top_customer_revenue = top_customers.iloc[0]['Total_Spent']
top_products_share = top_products['Total_Revenue'].sum() / total_revenue
peak_month = monthly_sales.iloc[monthly_sales['Total_Sales'].idxmax()]['Month']
peak_sales = monthly_sales['Total_Sales'].max()
uk_share = country_sales[country_sales['Country'] == 'United Kingdom']['Total_Sales'].iloc[0] / total_revenue

# Outliers (from EDA)
high_value_orders = df.groupby('Invoice')['TotalPrice'].sum()
high_value_orders = high_value_orders[high_value_orders > high_value_orders.quantile(0.99)]
low_price_items = df[df['Price'] < df['Price'].quantile(0.01)]['Description'].nunique()

# Export summary tables to Excel
with pd.ExcelWriter('summary.xlsx') as writer:
    country_sales.to_excel(writer, sheet_name='Sales by Country', index=False)
    top_products.to_excel(writer, sheet_name='Top Products', index=False)
    monthly_sales.to_excel(writer, sheet_name='Monthly Sales', index=False)
    top_customers.to_excel(writer, sheet_name='Top Customers', index=False)

print("Summary tables saved to summary.xlsx")