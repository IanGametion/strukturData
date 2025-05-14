class Array(object):
    def __init__(self, capacity, fillValue=None):
        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)
            
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __setitem__(self, index, newItem):
        self.items[index] = newItem
        
    def __getitem__(self,index):
        return self.items[index]
    
a = Array(5)
print(a)
for i in range(len(a)):
    a[i] = i + 1
    
