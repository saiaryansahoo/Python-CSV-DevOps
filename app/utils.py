# app/utils.py

import pandas as pd

def compute_monthly_revenue(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')
    monthly_revenue = df.groupby('month').apply(lambda x: (x['product_price'] * x['quantity']).sum())
    return monthly_revenue

def compute_product_revenue(df):
    product_revenue = df.groupby('product_name').apply(lambda x: (x['product_price'] * x['quantity']).sum())
    return product_revenue

def compute_customer_revenue(df):
    customer_revenue = df.groupby('customer_id').apply(lambda x: (x['product_price'] * x['quantity']).sum())
    return customer_revenue

def top_customers(customer_revenue, top_n=10):
    top_customers = customer_revenue.nlargest(top_n)
    return top_customers
