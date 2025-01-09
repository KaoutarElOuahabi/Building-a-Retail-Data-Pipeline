# Purpose: Handle database connections and queries.
import pandas as pd
from sqlalchemy import create_engine
import logging
from config.settings import DB_CONFIG

# Setting up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def connect_to_database():
    """Establish a connection to the PostgreSQL database using SQLAlchemy."""
    try:
        engine = create_engine(
            f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        )
        logger.info("Database connection successful.")
        return engine
    except Exception as e:
        logger.error(f"Error connecting to database: {e}")
        raise

def fetch_grocery_sales():
    """Fetch grocery sales data from the database."""
    query = """
        SELECT
            "index",
            "Store_ID",
            "Date",
            "Dept",
            "Weekly_Sales"
        FROM grocery_sales;
    """
    try:
        engine = connect_to_database()
        df = pd.read_sql_query(query, engine)
        logger.info("Data fetched successfully.")
        return df
    except Exception as e:
        logger.error(f"Error fetching data: {e}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        df = fetch_grocery_sales()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
