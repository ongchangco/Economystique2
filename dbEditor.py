import os
import sqlite3

path = os.path.join("db", "inventory_db.db")
conn = sqlite3.connect(path)
cursor = conn.cursor()

cursor.execute("DELETE FROM inventory WHERE inventory_id = 'test'")
conn.commit()
conn.close()