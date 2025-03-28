import sqlite3
import os
import pandas as pd

def fetch_sales_data():
    """ Fetch sales data and return a Pandas DataFrame with fixed month order. """
    db_path = os.path.join("db", "sales_db.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Define the fixed order of months
    fixed_order = [
        "january", "february", "march", "april", "may", "june", 
        "july", "august", "september", "october", "november", "december", "this_month"
    ]

    sales_data = {month: 0 for month in fixed_order}  # Initialize with zero sales

    # Fetch totals for each month
    for month in fixed_order:
        cursor.execute(f"SELECT SUM(price * quantity_sold) FROM {month}")
        total_sales = cursor.fetchone()
        sales_data[month] = total_sales[0] if total_sales and total_sales[0] is not None else 0

    conn.close()

    # Convert to Pandas DataFrame
    df = pd.DataFrame(list(sales_data.items()), columns=["Month", "TotalSales"])

    return df