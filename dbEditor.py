import os
import sqlite3


def edit_database():
    connectionPath = os.path.join("db", "prrestock_db.db")
    connection = sqlite3.connect(connectionPath)
    cursor = connection.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS restock_product (
        product_id TEXT PRIMARY KEY,
        product_name TEXT NOT NULL,
        amount INT NOT NULL DEFAULT 0,
        exp_date TEXT NOT NULL
    )
    """)
    
    cursor.execute("DELETE FROM restock_product WHERE product_id = 'C001'")
    
    connection.commit()
    connection.close()
    

    '''
    data = [
    ("C001", "Chocolate Moist Cake", 5, "04/15/25"),
    ("C002", "Yema Vanilla Cake", 5, "04/15/25"),
    ("C003", "Caramel Cake", 5, "04/15/25"),
    ("C004", "Ube Caramel Cake", 5, "04/15/25"),
    ("C005", "Red Velvet Cake", 5, "04/15/25"),
    ("C006", "Pandan Cake", 5, "04/15/25"),
    ("C007", "Strawberry Cake", 5, "04/15/25"),
    ("C008", "Biscoff Mocha Cake", 5, "04/15/25"),
    ("C009", "Bento Cake", 10, "04/15/25"),
    ("C010", "Cupcake", 20, "04/15/25")
    ]

    # Insert data
    cursor.executemany("""
    INSERT OR IGNORE INTO products_on_hand (product_id, product_name, on_hand, exp_date)
    VALUES (?, ?, ?, ?)
    """, data)
    '''
    

'''
path = os.path.join("db", "inventory_db.db")
conn = sqlite3.connect(path)
cursor = conn.cursor()

# DELETE
cursor.execute("DELETE FROM inventory WHERE inventory_id = 'test'")
conn.commit()
conn.close()'''
