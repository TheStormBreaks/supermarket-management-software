class ReceiptNode:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.next = None
        self.prev = None

class Receipt:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  # To track the number of items in the receipt

    def add_item(self, name, price):
        #Add item to the receipt
        new_node = ReceiptNode(name, price)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1  # Increment the size of the receipt

    def calculate_total(self):
        #calculate the receipt total
        current = self.head
        total = 0
        while current:
            total += current.price
            current = current.next
        return total

    def display_receipt(self):
        #print receipt
        if self.size == 0:
            print("No items in the receipt.")
            return
        print("\nReceipt:")
        current = self.head
        while current:
            print(f"Item: {current.name}, Price: {current.price}")
            current = current.next
        print(f"Total Cost: {self.calculate_total()}") 
        
        
        """


class DoublyLinkedList:
    class Node:
        def __init__ (self, name, price, ):
            self.name = name
            self.price = price"""

