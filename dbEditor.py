import os
import sqlite3

path = os.path.join("db", "restock_db.db")
conn = sqlite3.connect(path)
cursor = conn.cursor()

cursor.execute("DROP TABLE inventory")
conn.commit()
conn.close()