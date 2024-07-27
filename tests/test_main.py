# tests/test_main.py

import unittest
from app.main import main

class TestMain(unittest.TestCase):

    def test_main(self):
        # Redirect stdout to capture print statements for testing
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        main()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Monthly Revenue:", output)
        self.assertIn("Product Revenue:", output)
        self.assertIn("Customer Revenue:", output)
        self.assertIn("Top 10 Customers:", output)

if __name__ == '__main__':
    unittest.main()
