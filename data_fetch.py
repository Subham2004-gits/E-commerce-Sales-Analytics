
# data_fetch.py
import pandas as pd
from db_config import get_engine

def fetch_table(table_name):
    """Fetch entire table into Pandas DataFrame."""
    engine = get_engine()
    query = f'SELECT * FROM "{table_name}";'   # ensure case sensitivity for PG
    df = pd.read_sql(query, engine)
    return df

if __name__ == "__main__":
    # List of all tables in our schema
    tables = [
        "customers",
        "orders",
        "order_items",
        "products",
        "product_categories",
        "payments",
        "shipping",
        "coupons",
        "taxes",
        "currency_rates"
    ]

    dataframes = {}

    for table in tables:
        print(f"\nFetching {table}...")
        df = fetch_table(table)
        dataframes[table] = df
        print(df.head())  # show first 5 rows of each
