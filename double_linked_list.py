class DoublyLinkedList:
    class Node:
        __slots__ = 'element', 'prev', 'next'

        def __init__(self, element, prev = None, next = None):
            self.element = element
            self.prev = prev
            self.next = next

    def __init__(self):
        self.header = self.Node(None)
        self.trailer = self.Node(None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def insert_between(self, e, predessor, successor):
        newest = self.Node(e, predessor, successor)
        predessor.next = newest
        predessor.prev = newest
        self.size += 1
        return newest
    
    def delete_node(self, node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        element = node.element
        node.prev = node.next = node.element = None
        return element
    
    def display(self):
        current = dll.header.next
        while current != dll.trailer:
            print(current.element)
            current = current.next
        print("list end")

dll = DoublyLinkedList()

a = dll.insert_between(10, dll.header, dll.trailer)
dll.display()
b = dll.insert_between(20, a, dll.trailer)
dll.display()
c = dll.insert_between(15, a, b) 
dll.display()
dll.delete_node(b)  
dll.display()


class TryingToMakeCircularQueueWith(DoublyLinkedList):
    class Node:
        __slots__ = 'element', 'next'

        def __init__(self, element, next=None):
            self.element = element
            self.next = next

        def __init__(self):
            self.tail = None
            self.size = 0

        def __len__(self):
            return self.size
        
        def is_empty(self):
            return self.size == 0
        
        def first(self):
            if self.is_empty():
                raise Empty("Queue is empty")
            return self.tail.next
        
        def dequeue(self):
            delete_node()

