# Retail Sales Dashboard

Interactive Streamlit dashboard analyzing £14.7M in UK retail sales (2009–2011) from the UCI Online Retail II dataset.

# Live Demo
Explore the dashboard: https://retail-sales-dashboard-nieavlx7g6hb3zbcfpphiz.streamlit.app/
Project Overview
This project analyzes 800K+ retail transactions to uncover sales trends, customer behavior, and product performance. Key deliverables include:

Data Cleaning: Removed cancellations, handled missing values, and standardized formats using Python (Pandas).
SQL Analysis: Queried sales by country, products, and customers using SQLite.
EDA: Calculated metrics (e.g., £14.7M revenue, 5,917 customers) and visualized trends (e.g., November holiday peaks).
Dashboard: Built an interactive Streamlit app with Plotly charts and filters (country, date).
Insights: Proposed recommendations like 20% marketing budget for EIRE/Netherlands and 15% stock increase for top products.

# Key Findings

Revenue: £14,723,150, with 90% from the UK (£14.7M).
Customers: 5,917 unique, with top customers driving ~10% of revenue.
Trends: Sales peak in November 2010/2011 (£1.16M–£1.17M) due to holidays.
Products: "REGENCY CAKESTAND 3 TIER" (£286K) leads, contributing ~2% of revenue.
Outliers: 320 orders >£1000; 50 items <£0.20 need profitability review.

# Business Recommendations

Market Expansion: Allocate 20% of marketing budget to EIRE (£621K) and Netherlands (£554K) to grow non-UK share by 5% annually.
Inventory Optimization: Increase stock of top 5 products (e.g., "REGENCY CAKESTAND 3 TIER") by 15% for Q4 demand.
Customer Retention: Launch loyalty program with 5% discounts for top customers, targeting £500K additional sales.
Seasonal Strategy: Boost Q4 promotions by 25% to capture 10% revenue growth.
Profitability Review: Analyze 50 low-price items (<£0.20) for bundling to increase order value by £50.

# Visualizations



Sales by Country
(screenshots/sales_by_country.png)
Monthly Sales Trend
(screenshots/monthly_sales.png)









Top Products
(screenshots/top_products.png)
Order Value Distribution
(screenshots/order_value_distribution.png)






# Setup Instructions

Clone the repo:git clone https://github.com/Shashindra06/retail-sales-dashboard


Install dependencies:pip install -r requirements.txt


Run locally:streamlit run dashboard.py



# Technologies Used

Python (Pandas, Plotly, Streamlit)
SQLite
GitHub
Streamlit Community Cloud

# Contact

GitHub: 
LinkedIn: 
Email: shashindravadlakonda@gmail.com

