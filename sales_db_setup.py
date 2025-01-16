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
        quantity_sold INTEGER NOT NULL
    )
    """)
    
    '''
    data = [
    ("C001", "Chocolate Moist Cake", 850, 0),
    ("C002", "Yema Vanilla Cake", 760, 0),
    ("C003", "Caramel Cake", 820, 0),
    ("C004", "Ube Caramel Cake", 750, 0),
    ("C005", "Red Velvet Cake", 850, 0),
    ("C006", "Pandan Cake", 760, 0),
    ("C007", "Strawberry Cake", 780, 0),
    ("C008", "Biscoff Mocha Cake", 900, 0),
    ("C009", "Bento Cake", 370, 0),
    ("C010", "Cupcake", 40, 0)
    ]

    # Insert data
    cursor.executemany("""
    INSERT OR IGNORE INTO sales (product_id, product_name, price, quantity_sold)
    VALUES (?, ?, ?, ?)
    """, data)
    '''
    connection.commit()
    connection.close()