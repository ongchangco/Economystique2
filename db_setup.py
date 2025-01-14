import sqlite3, os

def inv_database():
    connectionPath = os.path.join("db", "inventory_db.db")
    connection = sqlite3.connect(connectionPath)
    cursor = connection.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        brand TEXT NOT NULL,
        unit TEXT NOT NULL,
        on_hand INTEGER NOT NULL,
        owed INTEGER NOT NULL DEFAULT 0,
        due_in INTEGER NOT NULL DEFAULT 0
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        price REAL NOT NULL,
        inventory_id INTEGER,
        FOREIGN KEY (inventory_id) REFERENCES inventory(inventory_id)
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
        sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        total_amount REAL NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sale_items (
        sale_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        sale_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity_sold INTEGER NOT NULL,
        price REAL NOT NULL,
        FOREIGN KEY (sale_id) REFERENCES sales(sale_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )
    """)

    connection.commit()
    connection.close()