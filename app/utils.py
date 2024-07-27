# app/utils.py

import pandas as pd

def compute_monthly_revenue(df):
    # Ensure 'order_date' is a datetime column
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')  # Extract month
    # Group by 'month' and calculate total revenue for each month
    monthly_revenue = df.groupby('month').agg(
        total_revenue=pd.NamedAgg(column='product_price', aggfunc=lambda x: (x * df.loc[x.index, 'quantity']).sum())
    ).reset_index()
    return monthly_revenue

def compute_product_revenue(df):
    # Group by 'product_name' and calculate total revenue for each product
    product_revenue = df.groupby('product_name').agg(
        total_revenue=pd.NamedAgg(column='product_price', aggfunc=lambda x: (x * df.loc[x.index, 'quantity']).sum())
    ).reset_index()
    return product_revenue

def compute_customer_revenue(df):
    # Group by 'customer_id' and calculate total revenue for each customer
    customer_revenue = df.groupby('customer_id').agg(
        total_revenue=pd.NamedAgg(column='product_price', aggfunc=lambda x: (x * df.loc[x.index, 'quantity']).sum())
    ).reset_index()
    return customer_revenue

def top_customers(customer_revenue):
    # Identify top 10 customers by revenue
    top_customers = customer_revenue.nlargest(10, 'total_revenue')
    return top_customers
