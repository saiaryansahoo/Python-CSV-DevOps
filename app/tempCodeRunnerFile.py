# app/main.py

import pandas as pd
from utils import compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, top_customers

def main():
    try:
        # Read the data
        df = pd.read_csv('D:\Task\data\orders.csv')

        # Compute the required metrics
        monthly_revenue = compute_monthly_revenue(df)
        product_revenue = compute_product_revenue(df)
        customer_revenue = compute_customer_revenue(df)
        top_customers_list = top_customers(customer_revenue)

        # Printing the results
        print("Monthly Revenue:\n", monthly_revenue)
        print("Product Revenue:\n", product_revenue)
        print("Customer Revenue:\n", customer_revenue)
        print("Top 10 Customers:\n", top_customers_list)
    
    #Exception Handling
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
