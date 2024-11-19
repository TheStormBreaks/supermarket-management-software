import sqlite3

def enqueue(serial_number, item_name, price, quantity):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("SELECT quantity FROM InventoryQueue WHERE serial_number = ?", (serial_number,))
    result = cursor.fetchone()

    if result:
        cursor.execute(
            "UPDATE InventoryQueue SET quantity = quantity + ? WHERE serial_number = ?",
            (quantity, serial_number),
        )
    else:
        cursor.execute(
            "INSERT INTO InventoryQueue (serial_number, item_name, price, quantity) VALUES (?, ?, ?, ?)",
            (serial_number, item_name, price, quantity),
        )

    conn.commit()
    conn.close()

def dequeue(serial_number):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("SELECT quantity FROM InventoryQueue WHERE serial_number = ?", (serial_number,))
    result = cursor.fetchone()

    if result:
        quantity = result[0]
        if quantity > 1:
            cursor.execute(
                "UPDATE InventoryQueue SET quantity = quantity - 1 WHERE serial_number = ?",
                (serial_number,),
            )
        else:
            cursor.execute("DELETE FROM InventoryQueue WHERE serial_number = ?", (serial_number,))
    else:
        print("Item not found!")

    conn.commit()
    conn.close()
