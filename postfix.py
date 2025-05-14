from stack import Stack

def mathOpr(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    
def postfixEval(postfixExp):
    tokenlst = postfixExp.split()
    lenLst = len(tokenlst)
    oprdStack = Stack(lenLst)
    for token in tokenlst:
        if token in '0123456789':
            oprdStack.push(int(token))
        else:
            oprd2 = oprdStack.pop()
            oprd1 = oprdStack.pop()
            result = mathOpr(token, oprd1, oprd2)
            oprdStack.push(result)
    return oprdStack.pop()