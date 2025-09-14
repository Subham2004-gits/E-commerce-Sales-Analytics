# eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the analytics-ready dataset
df = pd.read_csv("final_analytics_ready.csv")

# -------------------------------
# 1. Basic overview
# -------------------------------
print("Dataset shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nMissing values:\n", df.isna().sum())
print("\nData types:\n", df.dtypes)
print("\nFirst 5 rows:\n", df.head())

# -------------------------------
# 2. Revenue & Order Analysis
# -------------------------------
# Total revenue
total_revenue = df['line_total'].sum()
print(f"\nTotal Revenue: {total_revenue}")

# Revenue per order
revenue_per_order = df.groupby('ord_id')['line_total'].sum().reset_index()
plt.figure(figsize=(10,5))
sns.histplot(revenue_per_order['line_total'], bins=20, kde=True)
plt.title("Revenue Distribution per Order")
plt.xlabel("Order Total")
plt.ylabel("Frequency")
plt.show()

# Orders by status
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='order_status')
plt.title("Orders by Status")
plt.show()

# -------------------------------
# 3. Top Products
# -------------------------------
top_products = df.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Quantity Sold:\n", top_products)

plt.figure(figsize=(10,6))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Total Quantity Sold")
plt.ylabel("Product")
plt.show()

# -------------------------------
# 4. Coupon Usage
# -------------------------------
coupon_usage = df['coupon_code'].fillna("No Coupon").value_counts()
print("\nCoupon Usage:\n", coupon_usage)

plt.figure(figsize=(8,5))
sns.barplot(x=coupon_usage.index, y=coupon_usage.values, palette="magma")
plt.title("Coupon Usage Counts")
plt.xticks(rotation=45)
plt.show()

# -------------------------------
# 5. Trends over time
# -------------------------------
df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.month
df['day_of_week'] = df['order_date'].dt.day_name()

# Orders per month
orders_per_month = df.groupby('month')['ord_id'].nunique()
plt.figure(figsize=(8,5))
sns.lineplot(x=orders_per_month.index, y=orders_per_month.values, marker='o')
plt.title("Orders Per Month")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.show()

# Orders by day of week
orders_per_day = df.groupby('day_of_week')['ord_id'].nunique().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
)
plt.figure(figsize=(8,5))
sns.barplot(x=orders_per_day.index, y=orders_per_day.values, palette="coolwarm")
plt.title("Orders by Day of Week")
plt.xlabel("Day")
plt.ylabel("Number of Orders")
plt.show()

print("\nEDA completed successfully!")
