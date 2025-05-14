class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item): # menambahkan node
        self.items.append(item)
        
    def pop(self): # membuang node
        return self.items.pop()
    
    def isEmpty(self): # cek kosong atau tidak
        return (self.items == [])
    
    def peek(self): # melihat item paling atas
        return self.items[-1] 
    
    def __str__(self): 
        return str(self.items)
    
def isPalindrome(str):
    strStack = Stack()
    palindrome = False
    for char in str:
        strStack.push(char)
    for char in str:
        if (char == strStack.pop()):
            palindrome = True
        else:
            palindrome = False
    return palindrome

print(isPalindrome("bob"))