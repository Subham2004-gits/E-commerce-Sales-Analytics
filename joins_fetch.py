# joins_fetch.py
import pandas as pd
from db_config import get_engine

# Global engine for all functions
engine = get_engine()

def fetch_orders_with_customers():
    """Join Orders with Customers"""
    query = """
    SELECT o.ord_id, o.order_date, o.total_amt,
           c.first_name, c.last_name, c.email
    FROM orders o
    JOIN customers c ON o.cust_id = c.cust_id;
    """
    return pd.read_sql(query, engine)

def fetch_orders_with_items_products():
    """Join Orders → OrderItems → Products"""
    query = """
    SELECT o.ord_id, o.order_date, o.total_amt,
           p.name AS product_name, oi.quantity, oi.line_total
    FROM orders o
    JOIN order_items oi ON o.ord_id = oi.ord_id
    JOIN products p ON oi.prod_id = p.prod_id;
    """
    return pd.read_sql(query, engine)

def fetch_orders_with_payments():
    """Join Orders with Payments"""
    query = """
    SELECT o.ord_id, o.order_date, o.total_amt,
           pmt.pay_id, pmt.method , pmt.payment_date
    FROM orders o
    JOIN payments pmt ON o.ord_id = pmt.ord_id;
    """
    return pd.read_sql(query, engine)

def fetch_orders_with_shipping():
    """Join Orders with Shipping info (optional)"""
    query = """
   SELECT o.ord_id, o.order_date, o.total_amt,
           s.ship_id, s.ship_address, s.ship_date, s.delivery_date, s.status, s.tracking_no
    FROM orders o
    JOIN shipping s ON o.ord_id = s.ord_id;
    """
    return pd.read_sql(query, engine)


if __name__ == "__main__":
    print("Orders + Customers:\n", fetch_orders_with_customers().head())
    print("\nOrders + Items + Products:\n", fetch_orders_with_items_products().head())
    print("\nOrders + Payments:\n", fetch_orders_with_payments().head())
    # Uncomment if shipping table exists
    print("\nOrders + Shipping:\n", fetch_orders_with_shipping().head())
