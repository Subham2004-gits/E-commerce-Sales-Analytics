# get_joined_data.py
import pandas as pd
from data_fetch import fetch_table

def get_joined_data():
    """Join all relevant tables into a single DataFrame."""
    # Fetch tables
    customers = fetch_table("customers")
    orders = fetch_table("orders")
    order_items = fetch_table("order_items")
    products = fetch_table("products")
    payments = fetch_table("payments")
    shipping = fetch_table("shipping")
    coupons = fetch_table("coupons")

    # Join steps
    df = orders.merge(customers, on="cust_id", how="left") \
               .merge(order_items, on="ord_id", how="left") \
               .merge(products, left_on="prod_id", right_on="prod_id", how="left") \
               .merge(payments, on="ord_id", how="left") \
               .merge(shipping, on="ord_id", how="left") \
               .merge(coupons, on="coupon_code", how="left")
    
    return df

# Test join
if __name__ == "__main__":
    df_joined = get_joined_data()
    print(df_joined)
