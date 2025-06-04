class Point:
    def __init__(self, row = 0, col = 0):
        self.row = row
        self.col = col
    
class Stack:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.top = -1
        
    def is_empty(self):
        return self.top == -1
    
    def push(self, item):
        self.top += 1
        self.items[self.top] = item
        
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            exit(1)
        item = self.items[self.top]
        self.top -= 1
        return item
    
    