class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, number):
        # Add an element to the end of the queue.
        self.items.append(number)
        
    def dequeue(self):
        # Remove an element from the front of the queue.
        self.items.pop(0)
        
    def get_front(self):
        if(self.is_empty()):
            return "Queue underflow"
        return self.items[0]
    
    def get_rear(self):
        if(self.is_empty()):
            return "Queue underflow"
        return self.items[len(self.items) - 1]
        
    def is_empty(self):
        # Check if the queue is empty.
        if(len(self.items) == 0):
            return True
        return False
        
    def size(self):
        # Return the number of elements in the queue.
        return len(self.items)
        
    def display(self):
        # Print the elements in the queue.
        return self.items
        

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.size())
print(queue.get_front())
print(queue.get_rear())
print(queue.display())
queue.dequeue()
print(queue.is_empty())
print(queue.size())
print(queue.get_front())
print(queue.get_rear())
print(queue.display())
queue.dequeue()
queue.dequeue()
print(queue.is_empty())
print(queue.size())
print(queue.get_front())
print(queue.get_rear())
print(queue.display())
