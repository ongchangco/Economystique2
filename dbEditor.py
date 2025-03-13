import os
import sqlite3


def edit_database():
    connectionPath = os.path.join("db", "inventory_db.db")
    connection = sqlite3.connect(connectionPath)
    cursor = connection.cursor()

    # Edit Cell
    # cursor.execute("UPDATE inventory SET rop = ? WHERE inventory_id = ?;",(5000,"IN001"))
    
    # Create tables
    '''cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingredients (
        inventory_id TEXT PRIMARY KEY,
        description TEXT NOT NULL,
        C001 FLOAT NOT NULL,
        C002 FLOAT NOT NULL,
        C003 FLOAT NOT NULL,
        C004 FLOAT NOT NULL,
        C005 FLOAT NOT NULL,
        C006 FLOAT NOT NULL,
        C007 FLOAT NOT NULL,
        C008 FLOAT NOT NULL,
        C009 FLOAT NOT NULL,
        C010 FLOAT NOT NULL
    )
    """)
    '''
    
    # Add Data
    '''
    data = [("IN001","All-Purpose Flour",200,200,200,200,200,200,200,200,70,20),
            ("IN002","Baking Powder",4,8,8,2,4,8,8,4,2,0.5),
            ("IN003","Baking Soda",4,0,0,0,4,0,0,4,2,0),
            ("IN004","Cocoa Powder",50,0,0,0,10,0,0,20,18,5),
            ("IN005","White Sugar",150,180,180,180,200,180,180,150,50,15),
            ("IN006","Brown Sugar",20,0,0,0,0,0,0,50,20,0),
            ("IN007","Confectioner's Sugar",0,0,150,150,0,0,0,0,50,0),
            ("IN008","Butter",100,120,120,120,120,120,120,100,70,10),
            ("IN009","Cream Cheese",0,0,0,0,200,0,0,0,0,0),
            ("IN010","Vegetable Oil",50,0,0,0,0,0,0,50,15,0),
            ("IN011","Vanilla Extract",0,5,5,5,5,0,5,0,3,1),
            ("IN012","Milk",200,200,200,150,150,150,150,150,55,15),
            ("IN013","Eggs",0,3,3,3,2,3,3,2,1,1)    
    ]
    
    cursor.executemany("""
    INSERT OR IGNORE INTO ingredients (inventory_id, description, C001, C002, C003, C004, C005, C006, C007, C008, C009, C010)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, data)
    '''
    connection.commit()
    connection.close()
# DELETE
# cursor.execute("DELETE FROM inventory WHERE inventory_id = 'test'")


edit_database()