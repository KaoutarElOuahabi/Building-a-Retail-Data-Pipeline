# Purpose: Handle file operations (reading and writing Parquet files).
# file_handler.py: Read Parquet File
import pandas as pd


def read_file(file_path):
    """Read data from a parquet file."""
    try:
        df = pd.read_parquet(file_path)
        return df
    except Exception as e:
        raise Exception(f"Error reading file: {e}")

