📊 E-Commerce Sales Analytics Dashboard
🔹 Objective of the Project

The primary objective of this project is to design and develop a predictive and interactive e-commerce sales analytics dashboard that helps businesses understand customer behavior, track sales performance, identify top-selling products, and forecast future sales. Unlike a static dashboard, this solution integrates machine learning pipelines to provide intelligent insights through customer segmentation and sales forecasting, enabling better business decision-making.

🔹 Database Tables & Relationships

To simulate real-world e-commerce transactions, we structured the data into tables that reflect customers, orders, products, and payments. Using SQL-style relationships, we created multiple joins to fetch consolidated insights. The tables include:

Customers Table – Contains customer details like ID and segment.

Orders Table – Tracks order date, quantity, and product mapping.

Products Table – Stores product-level details such as price and name.

Payments Table – Records payment modes and timestamps.

Through JOIN operations, we combined these tables to generate a complete sales dataset. For example, by joining orders with customers and products, we were able to calculate metrics like customer lifetime value (CLV), average order value (AOV), and product-wise performance.

🔹 Exploratory Data Analysis (EDA)

The next step was to perform EDA (Exploratory Data Analysis) to understand hidden patterns in sales and customer behavior. We used a combination of Python libraries:

Pandas → Data manipulation and cleaning.

Seaborn & Matplotlib → Visualization of sales trends, correlations, and distributions.

Scikit-learn → Applied clustering and regression models.

Plotly → Built interactive charts later used in the dashboard.

The EDA revealed insights such as:

Monthly sales growth patterns.

Seasonal variations in customer purchases.

Top-selling products and their contribution to revenue.

Customer purchase frequency and segmentation opportunities.

🔹 Feature Engineering

Feature engineering played a key role in making the dataset ML-ready. We extracted new features like:

Order Total → Derived from quantity × unit price.

Monthly Sales Aggregates → Summarized transactions by month/year.

Customer Lifetime Value (CLV) → Estimated long-term customer contribution.

Recency, Frequency, Monetary (RFM) Scores → Captured customer behavior.

These engineered features provided the foundation for customer segmentation and sales forecasting models.

🔹 Streamlit Integration

After feature engineering, the data was integrated into Streamlit to create an interactive dashboard. Unlike static charts, Streamlit allowed dynamic filtering by:

Month

Product

Customer cluster

The dashboard included:

KPI Cards (Total Sales, Customers, Avg Order Value)

Monthly Sales Trends (line chart)

Customer Segmentation (scatter plots with clusters)

Top Products Analysis (bar chart)

Sales Forecasting (next-month prediction using regression)

This made the project more interactive, user-friendly, and visually appealing for business stakeholders.

🔹 ML Pipelines

The machine learning part of the project was modularized into pipelines for better organization and reusability. The pipelines included:

Feature Engineering Pipeline – Automated feature extraction and transformations.

Customer Segmentation Pipeline – Applied K-Means clustering to group customers based on spending and behavior.

Sales Forecasting Pipeline – Used Linear Regression to predict next month’s sales.

By modularizing these steps into pipelines, we ensured scalability and maintainability, allowing businesses to plug in fresh data without rewriting code.

🔹 Business Impact of Features

The features developed in this dashboard can significantly impact business growth:

Customer Segmentation → Helps in personalized marketing campaigns.

Sales Forecasting → Assists in inventory planning and resource allocation.

Top Products Analysis → Guides promotional strategies and bundling.

KPI Tracking → Provides executives with real-time insights for decision-making.

🔹 Pros & Cons of the Analytics Dashboard

✅ Pros:

Interactive and user-friendly dashboard.

Integrates machine learning models with visualization.

Scalable pipeline-based structure.

Helps businesses make data-driven decisions.

⚠️ Cons:

Forecasting is basic (Linear Regression); advanced models (Prophet, LSTM) could improve accuracy.

Dataset is currently limited in size; results may differ on large-scale data.

Requires real-time database connection for production use.

🔹 Conclusion

This project goes beyond traditional dashboards by embedding machine learning intelligence into sales analytics. With modular pipelines, feature engineering, and Streamlit integration, it creates a bridge between raw data and actionable insights—helping businesses understand customers, optimize operations, and plan for the future. 🚀