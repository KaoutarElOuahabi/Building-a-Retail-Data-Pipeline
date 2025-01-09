# Purpose: Orchestrate the Extract, Transform, Load (ETL) pipeline.
import pandas as pd
import logging
from datetime import datetime


from pipeline import database
from pipeline.file_handler import read_file
from pipeline.transformations import transform
from config.settings import INPUT_FILE, OUTPUT_FILE



# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def etl():

    # Start timer
    start_time = datetime.now()
    logging.info("Starting ETL pipeline: Fetching data from database.")

    try:

        # Simulate steps in the ETL process

        # Extract
        logging.info("Establishing database connection and fetching data.")
        db_data = database.fetch_grocery_sales()
        logging.info("Database data fetched successfully.")
        
        logging.info("Reading data from input file.")
        file_data = read_file(INPUT_FILE)
        logging.info("Input file data read successfully.")

        
        # Merge on 'index' (assuming 'index' exists in both datasets)
        logging.info("Merging database data with file data.")
        merged_data = pd.merge(db_data, file_data, on='index')
        logging.info("Data merged successfully.")  
        

        # Transform
        logging.info("Applying data transformations.")
        cleaned_df = transform(merged_data)
        logging.info("Transformations applied successfully.")


        # Load
        logging.info(f"Saving transformed data to {OUTPUT_FILE}.")
        cleaned_df.to_csv(OUTPUT_FILE, index=False)
        logging.info("Data saved successfully.")

        # Calculate and log elapsed time
        end_time = datetime.now()
        elapsed_time = end_time - start_time
        logging.info(f"Pipeline completed successfully. Time taken: {elapsed_time}.")


        # Simulate pipeline success
        end_time = datetime.now()
        elapsed_time = end_time - start_time

    except Exception as e:
        logging.error(f"Pipeline failed with error: {e}")



# Test your pipeline with small datasets to ensure everything works as expected.
# Add logging in etl.py to track progress:

