# Purpose: Perform transformations.
import pandas as pd
import logging 


# setup the logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def transform(merged_data):
    df =  merged_data.copy()
    # transforming the data 
    try :
        # 1. Fill missing numerical values
        df['CPI'] = df['CPI'].fillna(df['CPI'].median())
        df['Unemployment'] = df['Unemployment'].fillna(df['Unemployment'].median())
        df['Date'] = df['Date'].ffill().bfill()

        # 2. Add a column "Month" extracted from the Date column
        df['Month'] = pd.to_datetime(df['Date']).dt.month

        # 3. Keep rows where Weekly Sales are over $10,000
        df = df[df['Weekly_Sales'] > 10000]

        # 4. Keep only the required columns
        clean_data = df[['Store_ID', 'Month', 'Dept', 'IsHoliday', 'Weekly_Sales', 'CPI', 'Unemployment']]

        # Return the cleaned DataFrame
        return clean_data
    except Exception as e:
        logger.error(f'Error Transforming data {e}')
        raise


