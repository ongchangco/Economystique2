import os
import sqlite3


def edit_database():
    connectionPath = os.path.join("db", "sales_db.db")
    connection = sqlite3.connect(connectionPath)
    cursor = connection.cursor()

    # ADD COLUMN
    # cursor.execute("ALTER TABLE restock ADD COLUMN rop FLOAT DEFAULT 0")
    
    # EDIT CELL
    #cursor.execute("UPDATE inventory SET on_hand = ? WHERE inventory_id = ?;",(1000,"IN019"))
    
    # DELETE
    #cursor.execute("DELETE FROM inventory WHERE inventory_id = '321'")
    
    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS y2024 (
        product_id TEXT PRIMARY KEY,
        product_name TEXT NOT NULL,
        price FLOAT NOT NULL,
        quantity_sold int NOT NULL
    )
    """)
    
    
    # Add Data
    '''
    data = [("C001", "Chocolate Moist Cake", "850", 20),
            ("C002", "Yema Vanilla Cake", "760", 17),
            ("C003", "Caramel Cake", "820", 14),
            ("C004", "Ube Caramel Cake", "750", 18),
            ("C005", "Red Velvet Cake", "850", 24),
            ("C006", "Pandan Cake", "760", 11),
            ("C007", "Strawberry Cake", "780", 19),
            ("C008", "Biscoff Mocha Cake", "900", 23),
            ("C009", "Bento Cake", "370", 34),
            ("C010", "Cupcake", "40", 82),
            
    ]
    
    cursor.executemany("""
    INSERT OR IGNORE INTO december (product_id, product_name, price, quantity_sold)
    VALUES (?, ?, ?, ?)
    """, data)'''
    
    connection.commit()
    connection.close()
edit_database()