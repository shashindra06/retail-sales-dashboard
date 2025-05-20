import pandas as pd
import sqlite3

# Connect to database
conn = sqlite3.connect('retail.db')

# Query 1: Total sales by country (top 5)
query1 = '''
SELECT Country, SUM(TotalPrice) as Total_Sales
FROM sales
GROUP BY Country
ORDER BY Total_Sales DESC
LIMIT 5
'''
sales_by_country = pd.read_sql(query1, conn)
print("Top 5 Countries by Sales:")
print(sales_by_country)

# Query 2: Top 5 products by revenue
query2 = '''
SELECT Description, SUM(TotalPrice) as Total_Revenue
FROM sales
GROUP BY Description
ORDER BY Total_Revenue DESC
LIMIT 5
'''
top_products = pd.read_sql(query2, conn)
print("\nTop 5 Products by Revenue:")
print(top_products)

# Query 3: Monthly sales trend
query3 = '''
SELECT strftime('%Y-%m', InvoiceDate) as Month, SUM(TotalPrice) as Total_Sales
FROM sales
GROUP BY Month
ORDER BY Month
'''
monthly_sales = pd.read_sql(query3, conn)
print("\nMonthly Sales Trend:")
print(monthly_sales)

# Query 4: Top customers by revenue
query4 = '''
SELECT "Customer ID", SUM(TotalPrice) as Total_Spent
FROM sales
GROUP BY "Customer ID"
ORDER BY Total_Spent DESC
LIMIT 5
'''
top_customers = pd.read_sql(query4, conn)
print("\nTop 5 Customers by Revenue:")
print(top_customers)

# Close connection
conn.close()

# Save results to CSV for reference
sales_by_country.to_csv('sales_by_country.csv', index=False)
top_products.to_csv('top_products.csv', index=False)
monthly_sales.to_csv('monthly_sales.csv', index=False)
top_customers.to_csv('top_customers.csv', index=False)
print("\nQuery results saved to CSV files")