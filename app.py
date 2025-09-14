# app.py
import pandas as pd
import streamlit as st
import plotly.express as px
from pipelines import feature_engineering, customer_segmentation, sales_forecasting

# =========================
# 1️⃣ Sample Data
# =========================
data = {
    'cust_id': ['C1','C2','C3','C1','C2','C4','C5','C3','C1','C5','C2','C3','C4','C5','C1'],
    'order_date': pd.date_range(start='2025-01-01', periods=15, freq='15D'),
    'quantity': [1,2,3,2,1,4,1,2,3,1,2,3,2,1,4],
    'unit_price': [100,200,150,120,220,130,300,110,180,250,200,170,210,190,160],
    'name': ['Prod A','Prod B','Prod C','Prod A','Prod B','Prod D','Prod E','Prod C','Prod A','Prod E','Prod B','Prod C','Prod D','Prod E','Prod A']
}
df = pd.DataFrame(data)

# =========================
# 2️⃣ Feature Engineering
# =========================
df = feature_engineering(df)

# =========================
# 3️⃣ Customer Segmentation
# =========================
customer_data, df = customer_segmentation(df, n_clusters=2)

# =========================
# 4️⃣ Sales Forecasting
# =========================
monthly_sales, next_month_sales = sales_forecasting(df)

# =========================
# 5️⃣ Streamlit Dashboard
# =========================
st.set_page_config(page_title="E-Commerce Sales Analytics", layout="wide")
st.title("📊 E-Commerce Sales Analytics Dashboard")

# -------------------------
# Sidebar Filters
# -------------------------
st.sidebar.header("Filters")
selected_months = st.sidebar.multiselect(
    "Select Month(s)", options=sorted(df['month'].unique()), default=sorted(df['month'].unique()))
selected_products = st.sidebar.multiselect(
    "Select Product(s)", options=df['name'].unique(), default=df['name'].unique())
selected_clusters = st.sidebar.multiselect(
    "Select Cluster(s)", options=df['cluster'].unique(), default=df['cluster'].unique())

df_filtered = df[(df['month'].isin(selected_months)) &
                 (df['name'].isin(selected_products)) &
                 (df['cluster'].isin(selected_clusters))]

# -------------------------
# KPI Cards
# -------------------------
total_sales = df_filtered['order_total'].sum()
total_customers = df_filtered['cust_id'].nunique()
avg_order_value = df_filtered['order_total'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Customers", total_customers)
col3.metric("Avg Order Value", f"${avg_order_value:,.2f}")

st.markdown("---")

# -------------------------
# 1️⃣ Monthly Sales
# -------------------------
monthly_sales_filtered = df_filtered.groupby(['year','month'])['order_total'].sum().reset_index()
fig_sales = px.line(monthly_sales_filtered, x='month', y='order_total', title="Monthly Sales")
st.plotly_chart(fig_sales, use_container_width=True)

# -------------------------
# 2️⃣ Customer Segmentation (Dynamic)
# -------------------------
customer_filtered = customer_data[customer_data['cluster'].isin(selected_clusters)].reset_index()
fig_cluster = px.scatter(customer_filtered, x='order_total', y='CLV', color='cluster',
                         hover_data=['cust_id'], title="Customer Segmentation (K-Means)")
st.plotly_chart(fig_cluster, use_container_width=True)

# -------------------------
# 3️⃣ Top Products Sold
# -------------------------
top_products = df_filtered.groupby('name')['quantity'].sum().sort_values(ascending=False).head(10).reset_index()
fig_top = px.bar(top_products, x='name', y='quantity', title="Top 10 Products Sold")
st.plotly_chart(fig_top, use_container_width=True)

# -------------------------
# 4️⃣ Sales Forecasting
# -------------------------
st.subheader("📈 Sales Forecasting")
st.write(f"Predicted sales for next month: **${next_month_sales:,.2f}**")
st.success("Interactive & predictive dashboard ready! 🚀")
