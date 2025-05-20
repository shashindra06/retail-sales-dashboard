import streamlit as st
import pandas as pd

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

# Placeholder for charts
st.header("Visualizations")
st.write("Charts will be added here.")