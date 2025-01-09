from pipeline.database import fetch_grocery_sales

def test_fetch_grocery_sales():
    print("Starting the test...")
    df = fetch_grocery_sales()
    print(f"DataFrame fetched with {len(df)} rows.")
    assert not df.empty, "The grocery_sales DataFrame is empty."
    assert "Store_ID" in df.columns, "Expected 'Store_ID' column not found."
    print("Test passed: Data fetched and validated successfully.")


if __name__ == "__main__":
    test_fetch_grocery_sales()
