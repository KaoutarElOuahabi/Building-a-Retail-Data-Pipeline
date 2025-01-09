import unittest
from pipeline.database  import connect_to_database

class TestDatabaseConnection(unittest.TestCase):

    def test_connection_success(self):
        """Test successful database connection."""
        engine = connect_to_database()
        self.assertIsNotNone(engine)

    def test_connection_failure(self):
        """Test database connection failure."""
        invalid_db_config = {
            'user': 'invalid_user',
            'password': 'invalid_password',
            'host': 'invalid_host',
            'port': '5432',
            'database': 'invalid_db'
        }
        with self.assertRaises(Exception):
            engine = connect_to_database(invalid_db_config)

if __name__ == "__main__":
    unittest.main()
