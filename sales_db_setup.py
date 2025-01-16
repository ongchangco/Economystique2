import sqlite3, os

def sales_database():
    connectionPath = os.path.join("db", "sales_db.db")
    connection = sqlite3.connect(connectionPath)
    cursor = connection.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        product_id TEXT PRIMARY KEY,
        product_name TEXT NOT NULL,
        price FLOAT NOT NULL,
        quantity_sold FLOAT NOT NULL
    )
    """)
    
    connection.commit()
    connection.close()