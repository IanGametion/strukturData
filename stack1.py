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
    
def inFixToPostFix(infixExpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    
    opStack = Stack()
    postfixLst = []
    tokenList = infixExpr.split()
    
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixLst.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                postfixLst.append(topToken)
                topToken = opStack.pop()
        else:
            while(not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixLst.append(opStack.pop())
            opStack.push(token)
            
    while not opStack.isEmpty():
        postfixLst.append(opStack.pop())
    return " ".join(postfixLst)

print(inFixToPostFix("1 + 2 / 6"))
