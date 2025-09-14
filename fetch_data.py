# fetch_data.py
import pandas as pd
from sqlalchemy import create_engine

# DB Connection
engine = create_engine('postgresql+psycopg2://postgres:Subham%402004@localhost:5432/Ecommerce_db')

def fetch_full_order_data():
    query = """
    SELECT 
        o.ord_id,
        o.order_date,
        o.status AS order_status,
        o.subtotal,
        o.discount_amt,
        o.tax_amt,
        o.total_amt,
        c.cust_id,
        c.first_name,
        c.last_name,
        c.email,
        c.phone,
        c.location AS customer_location,
        p.pay_id,
        p.method AS payment_method,
        p.payment_date,
        p.amount_paid,
        p.status AS payment_status,
        s.ship_id,
        s.ship_address,
        s.ship_date,
        s.delivery_date,
        s.status AS shipping_status,
        s.tracking_no,
        oi.order_item_id,
        pr.prod_id,
        pr.name AS product_name,
        pr.category AS product_category,
        pr.brand AS product_brand,
        pr.price AS product_price,
        pr.vat_rate,
        oi.quantity,
        oi.unit_price,
        oi.line_total,
        cp.coupon_code,
        cp.discount_pct
    FROM orders o
    LEFT JOIN customers c ON o.cust_id = c.cust_id
    LEFT JOIN payments p ON o.ord_id = p.ord_id
    LEFT JOIN shipping s ON o.ord_id = s.ord_id
    LEFT JOIN order_items oi ON o.ord_id = oi.ord_id
    LEFT JOIN products pr ON oi.prod_id = pr.prod_id
    LEFT JOIN coupons cp ON o.coupon_code = cp.coupon_code
    ORDER BY o.order_date;
    """
    df = pd.read_sql(query, engine)
    return df

# Test fetch
if __name__ == "__main__":
    df_orders = fetch_full_order_data()
    print(df_orders)
