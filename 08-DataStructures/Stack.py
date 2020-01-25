class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack)==0
stos=Stack()
stos.push(5)   
stos.push(7)        
stos.push(4)        
stos.push(6)        
stos.push(1)   
for i in range(3):
    print(stos.pop()) 