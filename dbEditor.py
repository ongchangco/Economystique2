import os
import sqlite3


def edit_database():
    connectionPath = os.path.join("db", "product_db.db")
    connection = sqlite3.connect(connectionPath)
    cursor = connection.cursor()

    # ADD COLUMN
    # cursor.execute("ALTER TABLE restock ADD COLUMN rop FLOAT DEFAULT 0")
    
    # EDIT CELL
    '''cursor.execute("UPDATE nov SET quantity_sold = ? WHERE product_id = ?;",(19,"C007"))
    cursor.execute("UPDATE this_month SET quantity_sold = ? WHERE product_id = ?;",(12,"C002"))
    cursor.execute("UPDATE this_month SET quantity_sold = ? WHERE product_id = ?;",(6,"C003"))
    cursor.execute("UPDATE this_month SET quantity_sold = ? WHERE product_id = ?;",(7,"C004"))
    cursor.execute("UPDATE this_month SET quantity_sold = ? WHERE product_id = ?;",(21,"C005"))
    cursor.execute("UPDATE this_month SET quantity_sold = ? WHERE product_id = ?;",(8,"C006"))
    cursor.execute("UPDATE this_month SET quantity_sold = ? WHERE product_id = ?;",(16,"C006"))
    cursor.execute("UPDATE this_month SET quantity_sold = ? WHERE product_id = ?;",(12,"C008"))
    cursor.execute("UPDATE this_month SET quantity_sold = ? WHERE product_id = ?;",(25,"C009"))
    cursor.execute("UPDATE this_month SET quantity_sold = ? WHERE product_id = ?;",(38,"C010"))
    '''
    
    # DELETE ENTRY
    #cursor.execute("DELETE FROM products_on_hand WHERE product_id = '123'")
    
    # DELETE TABLE
    #cursor.execute(f"DROP TABLE IF EXISTS january")
    
    # EDIT TABLE NAME
    #cursor.execute("ALTER TABLE this_month RENAME TO apr")
    
    # CREATE TABLE
    '''cursor.execute("""
    CREATE TABLE IF NOT EXISTS year_total (
        product_id TEXT PRIMARY KEY,
        product_name TEXT NOT NULL,
        price FLOAT NOT NULL,
        quantity_sold int NOT NULL
    )
    """)'''
    
    
    # ADD DATA
    
    '''data = [("C001", "Chocolate Moist Cake", "850", 2),
            ("C002", "Yema Vanilla Cake", "760", 0),
            ("C003", "Caramel Cake", "820", 0),
            ("C004", "Ube Caramel Cake", "750", 1),
            ("C005", "Red Velvet Cake", "850", 5),
            ("C006", "Pandan Cake", "760", 0),
            ("C007", "Strawberry Cake", "780", 1),
            ("C008", "Biscoff Mocha Cake", "900", 0),
            ("C009", "Bento Cake", "370", 8),
            ("C010", "Cupcake", "40", 13),
            
    ]
    
    cursor.executemany("""
    INSERT OR IGNORE INTO year_total (product_id, product_name, price, quantity_sold)
    VALUES (?, ?, ?, ?)
    """, data)'''
    
    # GET TOTAL PER YEAR
    '''cursor.execute("""
        INSERT INTO year_total (product_id, product_name, price, quantity_sold)
        SELECT 
            product_id, 
            product_name, 
            price, 
            SUM(quantity_sold)
        FROM (
            SELECT * FROM jan
            UNION ALL
            SELECT * FROM feb
            UNION ALL
            SELECT * FROM mar
            UNION ALL
            SELECT * FROM this_month
            UNION ALL
            SELECT * FROM may
            UNION ALL
            SELECT * FROM jun
            UNION ALL
            SELECT * FROM jul
            UNION ALL
            SELECT * FROM aug
            UNION ALL
            SELECT * FROM sep
            UNION ALL
            SELECT * FROM oct
            UNION ALL
            SELECT * FROM nov
            UNION ALL
            SELECT * FROM dec
        ) 
        GROUP BY product_id
        ON CONFLICT(product_id) DO UPDATE SET quantity_sold=excluded.quantity_sold;
        """)'''
    
    connection.commit()
    connection.close()
edit_database()