# tests/test_utils.py

import unittest
import pandas as pd
from app.utils import compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, top_customers

class TestUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = pd.DataFrame({
            'order_id': [1, 2, 3, 4],
            'customer_id': [101, 102, 101, 103],
            'order_date': ['2021-01-01', '2021-02-01', '2021-01-15', '2021-03-01'],
            'product_id': [1001, 1002, 1001, 1003],
            'product_name': ['Product A', 'Product B', 'Product A', 'Product C'],
            'product_price': [10.0, 20.0, 10.0, 30.0],
            'quantity': [1, 2, 3, 1]
        })

    def test_compute_monthly_revenue(self):
        result = compute_monthly_revenue(self.df)
        self.assertEqual(result.loc['2021-01'], 40.0)
        self.assertEqual(result.loc['2021-02'], 40.0)
        self.assertEqual(result.loc['2021-03'], 30.0)

    def test_compute_product_revenue(self):
        result = compute_product_revenue(self.df)
        self.assertEqual(result.loc['Product A'], 40.0)
        self.assertEqual(result.loc['Product B'], 40.0)
        self.assertEqual(result.loc['Product C'], 30.0)

    def test_compute_customer_revenue(self):
        result = compute_customer_revenue(self.df)
        self.assertEqual(result.loc[101], 40.0)
        self.assertEqual(result.loc[102], 40.0)
        self.assertEqual(result.loc[103], 30.0)

    def test_top_customers(self):
        customer_revenue = compute_customer_revenue(self.df)
        result = top_customers(customer_revenue)
        self.assertEqual(len(result), 3)
        self.assertEqual(result.index[0], 101)

if __name__ == '__main__':
    unittest.main()
