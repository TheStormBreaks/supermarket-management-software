from collections import deque

class Inventory:
    def __init__(self):
        self.queue = deque()

    def add_item(self, serial_number, name, price):
        #Add an item to the inventory.
        self.queue.append({"serial_number": serial_number, "name": name, "price": price})

    def remove_item(self, serial_number):
        #Remove an item from the inventory by serial number.
        for item in self.queue:
            if item["serial_number"] == serial_number:
                self.queue.remove(item)
                return item
        return None

    def display_inventory(self):
        #Display all items in inventory.
        print("\nCurrent Inventory:")
        for item in self.queue:
            print(f"Serial Number: {item['serial_number']}, Name: {item['name']}, Price: {item['price']}")



