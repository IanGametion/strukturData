class Stack:
    def __init__(self):
        self.items = []
        
    def push(self,c):
        self.items.append(c)
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            exit(1)
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0