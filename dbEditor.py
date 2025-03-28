import os
import sqlite3


def edit_database():
    connectionPath = os.path.join("db", "sales_db.db")
    connection = sqlite3.connect(connectionPath)
    cursor = connection.cursor()

    # ADD COLUMN
    # cursor.execute("ALTER TABLE restock ADD COLUMN rop FLOAT DEFAULT 0")
    
    # EDIT CELL
    cursor.execute("UPDATE this_month SET quantity_sold = ? WHERE product_id = ?;",(100,"C001"))
    cursor.execute("UPDATE this_month SET quantity_sold = ? WHERE product_id = ?;",(12,"C002"))
    cursor.execute("UPDATE this_month SET quantity_sold = ? WHERE product_id = ?;",(6,"C003"))
    cursor.execute("UPDATE this_month SET quantity_sold = ? WHERE product_id = ?;",(7,"C004"))
    cursor.execute("UPDATE this_month SET quantity_sold = ? WHERE product_id = ?;",(21,"C005"))
    cursor.execute("UPDATE this_month SET quantity_sold = ? WHERE product_id = ?;",(8,"C006"))
    cursor.execute("UPDATE this_month SET quantity_sold = ? WHERE product_id = ?;",(16,"C006"))
    cursor.execute("UPDATE this_month SET quantity_sold = ? WHERE product_id = ?;",(12,"C008"))
    cursor.execute("UPDATE this_month SET quantity_sold = ? WHERE product_id = ?;",(25,"C009"))
    cursor.execute("UPDATE this_month SET quantity_sold = ? WHERE product_id = ?;",(38,"C010"))
    
    # DELETE
    #cursor.execute("DELETE FROM inventory WHERE inventory_id = '321'")
    
    # Create tables
    '''cursor.execute("""
    CREATE TABLE IF NOT EXISTS this_month (
        product_id TEXT PRIMARY KEY,
        product_name TEXT NOT NULL,
        price FLOAT NOT NULL,
        quantity_sold int NOT NULL
    )
    """)'''
    
    
    # Add Data
    '''
    data = [("C001", "Chocolate Moist Cake", "850", 14),
            ("C002", "Yema Vanilla Cake", "760", 17),
            ("C003", "Caramel Cake", "820", 12),
            ("C004", "Ube Caramel Cake", "750", 14),
            ("C005", "Red Velvet Cake", "850", 24),
            ("C006", "Pandan Cake", "760", 8),
            ("C007", "Strawberry Cake", "780", 16),
            ("C008", "Biscoff Mocha Cake", "900", 21),
            ("C009", "Bento Cake", "370", 50),
            ("C010", "Cupcake", "40", 61),
            
    ]'''
    '''
    cursor.executemany("""
    INSERT OR IGNORE INTO this_month (product_id, product_name, price, quantity_sold)
    VALUES (?, ?, ?, ?)
    """, data)'''
    
    connection.commit()
    connection.close()
edit_database()