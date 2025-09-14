import psycopg2
import pandas as pd

# Database credentials
db_name = "Ecommerce_db"
db_user = "postgres"
db_password = "Subham@2004"   # replace with your actual password
db_host = "localhost"
db_port = "5432"

# Establish connection
conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

# Create a cursor (optional if running direct SQL queries)
cur = conn.cursor()

# Example: Fetch all customers into a pandas DataFrame
customers_df = pd.read_sql("SELECT * FROM customers;", conn)
print(customers_df)  


customers_df.head()       # first 5 rows
customers_df.info()       # columns and data types
customers_df.describe()   # statistical summary for numeric fields
customers_df.isnull().sum()  # check missing values

customers_df['phone'].fillna('Unknown', inplace=True)
customers_df.dropna(subset=['email'], inplace=True)


customers_df['phone'] = customers_df['phone'].fillna('Unknown')

# Fill missing values for specific columns
customers_df['phone'] = customers_df['phone'].fillna('Unknown')
customers_df['last_name'] = customers_df['last_name'].fillna('N/A')
customers_df['location'] = customers_df['location'].fillna('Unknown')

# OR, if you want to fill all object-type columns automatically
for col in customers_df.select_dtypes(include='object').columns:
    customers_df[col] = customers_df[col].fillna('Unknown')
