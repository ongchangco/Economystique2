import sqlite3, os

def ingredients_database():
    connectionPath = os.path.join("db", "ingredients_db.db")
    connection = sqlite3.connect(connectionPath)
    cursor = connection.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingredients (
        product_id TEXT PRIMARY KEY,
        IN001 FLOAT NOT NULL,
        IN002 FLOAT NOT NULL,
        IN003 FLOAT NOT NULL,
        IN004 FLOAT NOT NULL,
        IN005 FLOAT NOT NULL,
        IN006 FLOAT NOT NULL,
        IN007 FLOAT NOT NULL,
        IN008 FLOAT NOT NULL,
        IN009 FLOAT NOT NULL,
        IN010 FLOAT NOT NULL,
        IN011 FLOAT NOT NULL,
        IN012 FLOAT NOT NULL,
        IN013 FLOAT NOT NULL
    )
    """)
    
    connection.commit()
    connection.close()