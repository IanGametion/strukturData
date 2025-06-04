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
    
class Maze:
    ROWS = 15
    COLS = 15
    
    def __init__(self):
        self.stack = Stack(self.ROWS * self.COLS)
        self.matrix = [
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]
        ]
    
    def can_move(self, row, col):
        return (0 <= row < self.ROWS and 0 <= col < self.COLS and self. matrix[row][col] == 0)
    
    def print_maze(self):
        for row in self.matrix:
            print(" ".join(str(cell) for cell in row))