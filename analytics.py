# analytics.py
import pandas as pd
from get_joined_data import get_joined_data

def clean_and_transform(df):
    """Prepare analysis-ready DataFrame."""
    df = df.copy()

    # Handle missing values
    df['coupon_code'] = df['coupon_code'].fillna("No Coupon")
    df['discount_pct'] = df['discount_pct'].fillna(0)

    # Correct data types
    date_cols = ['order_date', 'payment_date', 'ship_date', 'delivery_date']
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    num_cols = ['subtotal', 'discount_amt', 'tax_amt', 'unit_price', 'line_total', 'total_amt', 'amount_paid']
    for col in num_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Derived fields
    df['final_price_per_item'] = df['unit_price'] * df['quantity']
    order_totals = df.groupby('ord_id')['line_total'].sum().reset_index()
    order_totals.rename(columns={'line_total':'order_total_calc'}, inplace=True)
    df = df.merge(order_totals, on='ord_id', how='left')

    # Date features
    df['order_year'] = df['order_date'].dt.year
    df['order_month'] = df['order_date'].dt.month
    df['order_day_of_week'] = df['order_date'].dt.day_name()

    return df

if __name__ == "__main__":
    df_joined = get_joined_data()
    df_clean = clean_and_transform(df_joined)
    print(df_clean)
