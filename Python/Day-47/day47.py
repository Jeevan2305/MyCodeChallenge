class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, number):
        self.stack.append(number)
    
    def pop(self):
        if self.stack == []:
            return "Stack underflow"
        res = self.stack[:len(self.stack)-1]
        self.stack = res
        return res

    def size(self):
        return len(self.stack)

    def display(self):
        return self.stack

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.display())  # Output: [1, 2, 3]
print(stack.size())  # Output: 3
stack.pop()
print(stack.display())  
print(stack.size())  
stack.pop()
stack.pop()
print(stack.display())  
print(stack.size()) 
