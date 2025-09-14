# eda_report.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("final_analytics_ready.csv")

# ===== Dataset Overview =====
print("===== Dataset Overview =====")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# ===== 1. Orders Over Time =====
df['order_date'] = pd.to_datetime(df['order_date'])
orders_over_time = df.groupby(df['order_date'].dt.date)['ord_id'].count()

plt.figure(figsize=(12,6))
sns.lineplot(x=orders_over_time.index, y=orders_over_time.values)
plt.title("Orders Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("orders_over_time.png")
plt.show()

# ===== 2. Top Products =====
# Use 'name' for product name
top_products = df.groupby("name")["quantity"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Total Quantity Sold")
plt.ylabel("Product Name")
plt.tight_layout()
plt.savefig("top_products.png")
plt.show()

# ===== 3. Revenue by Product Category =====
revenue_by_category = df.groupby("category")["line_total"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(x=revenue_by_category.values, y=revenue_by_category.index, palette="coolwarm")
plt.title("Revenue by Product Category")
plt.xlabel("Revenue")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig("revenue_by_category.png")
plt.show()

# ===== 4. Payment Method Distribution =====
payment_counts = df['method'].value_counts()

plt.figure(figsize=(8,5))
sns.barplot(x=payment_counts.index, y=payment_counts.values, palette="magma")
plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("payment_distribution.png")
plt.show()

# ===== 5. Coupon Usage =====
coupon_counts = df['coupon_code'].value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=coupon_counts.index, y=coupon_counts.values, palette="plasma")
plt.title("Top 10 Coupons Used")
plt.xlabel("Coupon Code")
plt.ylabel("Usage Count")
plt.tight_layout()
plt.savefig("top_coupons.png")
plt.show()

# ===== 6. Orders by Day of Week =====
orders_by_day = df['order_day_of_week'].value_counts().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])

plt.figure(figsize=(10,5))
sns.barplot(x=orders_by_day.index, y=orders_by_day.values, palette="Set2")
plt.title("Orders by Day of Week")
plt.xlabel("Day")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("orders_by_day.png")
plt.show()

print("\nEDA Completed! Plots saved as PNG files.")
