import os
import sqlite3


def edit_database():
    connectionPath = os.path.join("db", "product_db.db")
    connection = sqlite3.connect(connectionPath)
    cursor = connection.cursor()

    # ADD COLUMN
    # cursor.execute("ALTER TABLE restock ADD COLUMN rop FLOAT DEFAULT 0")
    
    # EDIT CELL
    cursor.execute("UPDATE products_on_hand SET on_hand = ? WHERE product_id = ?;",(0,"C002"))
    cursor.execute("UPDATE products_on_hand SET on_hand = ? WHERE product_id = ?;",(0,"C003"))
    cursor.execute("UPDATE products_on_hand SET on_hand = ? WHERE product_id = ?;",(0,"C010"))
    '''cursor.execute("UPDATE products_on_hand SET exp_date = ? WHERE product_id = ?;",("n/a","C004"))
    cursor.execute("UPDATE products_on_hand SET exp_date = ? WHERE product_id = ?;",("n/a","C005"))
    cursor.execute("UPDATE products_on_hand SET exp_date = ? WHERE product_id = ?;",("n/a","C006"))
    cursor.execute("UPDATE products_on_hand SET exp_date = ? WHERE product_id = ?;",("n/a","C007"))
    cursor.execute("UPDATE products_on_hand SET exp_date = ? WHERE product_id = ?;",("n/a","C008"))
    cursor.execute("UPDATE products_on_hand SET exp_date = ? WHERE product_id = ?;",("n/a","C009"))
    cursor.execute("UPDATE products_on_hand SET exp_date = ? WHERE product_id = ?;",("n/a","C010"))'''


    # DELETE ENTRY
    #cursor.execute("DELETE FROM products_on_hand WHERE product_id = 'C011'")
    
    # DELETE TABLE
    #cursor.execute(f"DROP TABLE IF EXISTS january")
    
    # EDIT TABLE NAME
    #cursor.execute("ALTER TABLE this_month RENAME TO apr")
    
    # CREATE TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS year_total (
        product_id TEXT PRIMARY KEY,
        product_name TEXT NOT NULL,
        price FLOAT NOT NULL,
        quantity_sold int NOT NULL
    )
    """)
    
    
    # ADD DATA
    '''data = [("C001", "Chocolate Moist Cake", "850", 20),
            ("C002", "Yema Vanilla Cake", "760", 15),
            ("C003", "Caramel Cake", "820", 21),
            ("C004", "Ube Caramel Cake", "750", 19),
            ("C005", "Red Velvet Cake", "850", 21),
            ("C006", "Pandan Cake", "760", 17),
            ("C007", "Strawberry Cake", "780", 23),
            ("C008", "Biscoff Mocha Cake", "900", 20),
            ("C009", "Bento Cake", "370", 51),
            ("C010", "Cupcake", "40", 95),
            
    ]
    
    cursor.executemany("""
    INSERT OR IGNORE INTO dec (product_id, product_name, price, quantity_sold)
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