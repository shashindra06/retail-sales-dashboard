import streamlit as st
import pandas as pd
import plotly.express as px

# Load cleaned data
df = pd.read_csv('online_retail_cleaned.csv')
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Title
st.title("Online Retail Sales Dashboard")
st.write("Interactive dashboard analyzing UK retail sales (2009–2011).")

# Sidebar: Filters
st.sidebar.header("Filters")
countries = ['All'] + sorted(df['Country'].unique().tolist())
selected_country = st.sidebar.selectbox("Select Country", countries)
start_date = st.sidebar.date_input("Start Date", df['InvoiceDate'].min())
end_date = st.sidebar.date_input("End Date", df['InvoiceDate'].max())

# Apply filters
filtered_df = df.copy()
if selected_country != 'All':
    filtered_df = filtered_df[filtered_df['Country'] == selected_country]
filtered_df = filtered_df[
    (filtered_df['InvoiceDate'] >= pd.to_datetime(start_date)) &
    (filtered_df['InvoiceDate'] <= pd.to_datetime(end_date))
]

# Metrics
st.header("Key Metrics")
total_revenue = filtered_df['TotalPrice'].sum()
unique_customers = filtered_df['Customer ID'].nunique()
avg_order_value = filtered_df.groupby('Invoice')['TotalPrice'].sum().mean()
total_orders = filtered_df['Invoice'].nunique()
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"£{total_revenue:,.2f}")
col2.metric("Unique Customers", f"{unique_customers:,}")
col3.metric("Average Order Value", f"£{avg_order_value:,.2f}")
col4.metric("Total Orders", f"{total_orders:,}")

# Visualizations
st.header("Visualizations")

# Chart 1: Sales by Country (Top 10)
country_sales = filtered_df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)
fig1 = px.bar(x=country_sales.values, y=country_sales.index, title='Top 10 Countries by Sales')
fig1.update_layout(xaxis_title='Total Sales (£)', yaxis_title='Country')
st.plotly_chart(fig1, use_container_width=True)

# Chart 2: Monthly Sales Trend
monthly_sales = filtered_df.groupby(filtered_df['InvoiceDate'].dt.strftime('%Y-%m'))['TotalPrice'].sum().reset_index()
fig2 = px.line(x=monthly_sales['InvoiceDate'], y=monthly_sales['TotalPrice'], title='Monthly Sales Trend')
fig2.update_layout(xaxis_title='Month', yaxis_title='Total Sales (£)')
st.plotly_chart(fig2, use_container_width=True)

# Chart 3: Top Products by Revenue
top_products = filtered_df.groupby('Description')['TotalPrice'].sum().sort_values(ascending=False).head(5)
fig3 = px.bar(x=top_products.values, y=top_products.index, title='Top 5 Products by Revenue')
fig3.update_layout(xaxis_title='Total Revenue (£)', yaxis_title='Product')
st.plotly_chart(fig3, use_container_width=True)

# Chart 4: Top Customers by Revenue
top_customers = filtered_df.groupby('Customer ID')['TotalPrice'].sum().sort_values(ascending=False).head(5)
fig4 = px.bar(x=top_customers.values, y=top_customers.index, title='Top 5 Customers by Revenue')
fig4.update_layout(xaxis_title='Total Spent (£)', yaxis_title='Customer ID')
st.plotly_chart(fig4, use_container_width=True)