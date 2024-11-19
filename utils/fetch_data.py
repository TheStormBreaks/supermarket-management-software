import sqlite3

def fetch_inventory():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM InventoryQueue")
    data = cursor.fetchall()

    conn.close()
    return data
