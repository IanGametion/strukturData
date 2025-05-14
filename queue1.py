class Queue:
    def __init__(self, limit=5):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0
    
    def isEmpty(self):
        return len(self.array) == 0
    
    def long(self):
        return len(self.array)
    
    def queFront(self):
        if self.isEmpty():
            return None
        return self.array[0]
    
    def addQue(self,data):
        self.array.append(data)
        
    def remQue(self):
        if self.isEmpty():
            print("Underflow")
            return None
        data = self.array[0]
        self.array.remove(data)
        return data