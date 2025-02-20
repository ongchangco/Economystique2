import sqlite3, os

def inv_database():
    connectionPath = os.path.join("db", "inventory_db.db")
    connection = sqlite3.connect(connectionPath)
    cursor = connection.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        inventory_id TEXT PRIMARY KEY,
        description TEXT NOT NULL,
        brand TEXT NOT NULL,
        unit TEXT NOT NULL,
        on_hand FLOAT NOT NULL DEFAULT 0
    )
    """)
    
    connection.commit()
    connection.close()