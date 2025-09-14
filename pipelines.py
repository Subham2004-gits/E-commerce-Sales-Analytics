# pipeline.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression

# =========================
# 1️⃣ Feature Engineering
# =========================
def feature_engineering(df):
    # Total order value
    df['order_total'] = df['quantity'] * df['unit_price']
    
    # Date features
    df['month'] = df['order_date'].dt.month
    df['year'] = df['order_date'].dt.year
    df['day_of_week'] = df['order_date'].dt.day_name()
    
    # Customer Lifetime Value (CLV)
    clv = df.groupby('cust_id')['order_total'].sum().reset_index()
    clv.columns = ['cust_id', 'CLV']
    df = df.merge(clv, on='cust_id', how='left')
    
    return df

# =========================
# 2️⃣ Customer Segmentation
# =========================
def customer_segmentation(df, n_clusters=2):
    customer_data = df.groupby('cust_id')[['order_total', 'CLV']].sum()
    
    # Scaling
    scaler = StandardScaler()
    customer_scaled = scaler.fit_transform(customer_data)
    
    # KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    customer_data['cluster'] = kmeans.fit_predict(customer_scaled)
    
    # Merge cluster info back to main df
    df = df.merge(customer_data['cluster'], on='cust_id', how='left')
    
    return customer_data, df

# =========================
# 3️⃣ Sales Forecasting
# =========================
def sales_forecasting(df):
    # Group by year & month
    monthly_sales = df.groupby(['year', 'month'])['order_total'].sum().reset_index()
    
    # Month number for linear regression
    monthly_sales['month_num'] = monthly_sales['year'] * 12 + monthly_sales['month']
    
    X = monthly_sales[['month_num']]
    y = monthly_sales['order_total']
    
    # Linear Regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict next month sales
    next_month_num = X['month_num'].max() + 1
    next_month_sales = model.predict([[next_month_num]])[0]
    
    return monthly_sales, next_month_sales
