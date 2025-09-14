# feature_engineering.py
import pandas as pd
import numpy as np

def create_features(df):
    # Convert dates
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['signup_date'] = pd.to_datetime(df['signup_date'])
    df['payment_date'] = pd.to_datetime(df['payment_date'])
    
    # Time-based features
    df['order_year'] = df['order_date'].dt.year
    df['order_month'] = df['order_date'].dt.month
    df['order_day_of_week'] = df['order_date'].dt.day_name()
    df['is_weekend'] = df['order_day_of_week'].isin(['Saturday','Sunday']).astype(int)
    
    # Customer-level aggregation for RFM
    rfm = df.groupby('cust_id').agg(
        recency=('order_date', lambda x: (df['order_date'].max() - x.max()).days),
        frequency=('ord_id', 'count'),
        monetary=('total_amt', 'sum'),
        avg_discount=('discount_amt', 'mean'),
        avg_items=('quantity', 'mean')
    ).reset_index()
    
    # Merge RFM back to main dataframe (optional)
    df = df.merge(rfm, on='cust_id', how='left')
    
    # Product-level features
    df['final_price_per_item'] = df['line_total'] / df['quantity']
    
    # Example categorical encoding (optional)
    df = pd.get_dummies(df, columns=['category', 'brand', 'location'], drop_first=True)
    
    return df, rfm

if __name__ == "__main__":
    df = pd.read_csv("final_analytics_ready.csv")
    df_features, df_rfm = create_features(df)
    df_features.to_csv("analytics_with_features.csv", index=False)
    df_rfm.to_csv("customer_rfm_features.csv", index=False)
    print("Feature engineering completed!")
