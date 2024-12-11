class CircularQueue:
    def __init__ (self, size, name, price, serial_number):
        self.size = size
        self.queue = [None] * size
        self.name = name
        self.price = price
        self.serial_number = serial_number
        self.front = -1
        self.rear = -1

    #Add new item in inventory
    def enqueue(self, data):
        #check if inventory is full
        if(self.rear + 1) % self.size == self.front:
            print("Inventory Full")
            return
        
        #add the first element
        if self.front == -1:
            self.front = 0

        #move rear pointer and add element
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print(f"Enqueued: {data}")

    #Remove item from inventory
    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return None
        
        data = self.queue[self.front]
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return data
    
    def display(self):
        if self.front == -1:
            print("empty queue")
            return
        
        print ("Circular Queue Elements: ")
        index = self.front
        while True:
            print(self.queue[index], end=" ")
            if index == self.rear:
                break
            index = (index + 1) % self.size
            print()
    
    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    

inventory = CircularQueue
inventory.enqueue({"serial_number": 1234, "name": 'Egg', "price": 50})

inventory.display()


