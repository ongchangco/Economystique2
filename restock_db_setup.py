import sqlite3, os

def restock_database():
    connectionPath = os.path.join("db", "restock_db.db")
    connection = sqlite3.connect(connectionPath)
    cursor = connection.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS restock (
        inventory_id TEXT PRIMARY KEY,
        description TEXT NOT NULL,
        brand TEXT NOT NULL,
        unit TEXT NOT NULL,
        amount FLOAT NOT NULL DEFAULT 0
    )
    """)
    
    # Dummy data
    '''
    data = [
    ("123123", "Test", "ex", "kg", 45)
    ]

    # Insert data
    cursor.executemany("""
    INSERT OR IGNORE INTO restock (inventory_id, description, brand, unit, amount)
    VALUES (?, ?, ?, ?, ?)
    """, data)
    '''
    
    connection.commit()
    connection.close()