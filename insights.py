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

# Write findings and recommendations
with open('eda_findings.txt', 'w') as f:
    f.write("Key EDA Findings\n")
    f.write(f"- Total Revenue: £{total_revenue:,.2f}\n")
    f.write(f"- Unique Customers: {unique_customers:,}\n")
    f.write(f"- Average Order Value: £{avg_order_value:,.2f}\n")
    f.write(f"- Total Orders: {total_orders:,}\n")
    f.write(f"- Top Customer ID: {top_customer_id}, Revenue: £{top_customer_revenue:,.2f}\n")
    f.write(f"- Country Sales: UK dominates with {uk_share:.0%} (£{country_sales.iloc[0]['Total_Sales']:,.0f}), followed by {country_sales.iloc[1]['Country']} (£{country_sales.iloc[1]['Total_Sales']:,.0f}), {country_sales.iloc[2]['Country']} (£{country_sales.iloc[2]['Total_Sales']:,.0f}).\n")
    f.write(f"- Top Products: \"{top_products.iloc[0]['Description']}\" (£{top_products.iloc[0]['Total_Revenue']:,.0f}) leads, indicating strong demand for premium gift-ware.\n")
    f.write(f"- Monthly Trends: Sales peak in {peak_month} (£{peak_sales:,.0f}), driven by holiday shopping.\n")
    f.write(f"- Outliers: {len(high_value_orders)} orders exceed £{high_value_orders.min():,.0f}, representing high-value transactions. {low_price_items} items priced below £{df[df['Price'] < df['Price'].quantile(0.01)]['Price'].min():,.2f} may need profitability review.\n")
    f.write("\nBusiness Recommendations\n")
    f.write(f"- Market Expansion: UK contributes {uk_share:.0%} of revenue, indicating over-reliance. Allocate 20% of marketing budget to {country_sales.iloc[1]['Country']} (£{country_sales.iloc[1]['Total_Sales']:,.0f}) and {country_sales.iloc[2]['Country']} (£{country_sales.iloc[2]['Total_Sales']:,.0f}) to grow non-UK share by 5% annually.\n")
    f.write(f"- Inventory Optimization: Top 5 products (e.g., \"{top_products.iloc[0]['Description']}\") account for ~{top_products_share:.0%} of revenue (£{top_products['Total_Revenue'].sum():,.0f} combined). Increase stock by 15% to meet demand, especially in Q4.\n")
    f.write(f"- Customer Retention: Top 5 customers (e.g., ID {top_customer_id}, £{top_customer_revenue:,.0f}) drive ~{top_customers['Total_Spent'].sum()/total_revenue:.0%} of revenue. Launch a loyalty program with 5% discounts to retain high-value clients, targeting £500K additional sales.\n")
    f.write(f"- Seasonal Strategy: November sales (£{peak_sales:,.0f}) represent ~{peak_sales/total_revenue:.0%} of annual revenue. Boost Q4 promotions (e.g., holiday bundles) by 25% to capture 10% revenue growth.\n")
    f.write(f"- Profitability Review: {low_price_items} items priced below £{df[df['Price'] < df['Price'].quantile(0.01)]['Price'].min():,.2f} (e.g., \"POSTAGE\") may erode margins. Analyze profitability and consider bundling with high-margin products to increase average order value by £50.\n")

print("Findings and recommendations saved to eda_findings.txt")