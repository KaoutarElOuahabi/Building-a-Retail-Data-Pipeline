import unittest
from pipeline.database import fetch_grocery_sales

class TestFetchData(unittest.TestCase):

    def test_fetch_data_success(self):
        """Test fetching data from the database."""
        data = fetch_grocery_sales()
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) > 0)

    def test_fetch_data_failure(self):
        """Test failure in fetching data."""
        with self.assertRaises(Exception):
            fetch_grocery_sales()  # Ensure database is down or other issues exist

if __name__ == "__main__":
    unittest.main()
