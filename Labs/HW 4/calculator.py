from list import DLinkedList as linkedList
from stack import Stack as stack
import sys

task = sys.argv[1]
operation = sys.argv[2:]

def convertToPost(operation):
    
    postfixOp = ''
    operators = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0, ')': 0} # Check if allowed to do this
    opStack = stack()

    while len(operation) > 0:
        item = operation[0]
        operation = operation[1:]
        
        if item not in ';()' and operators.get(item) == None:
            postfixOp+=item
            
        else:
            if item == '(':
                opStack.push(item)
                
            elif item not in '()' and operators.get(item) != None:
                while not opStack.isEmpty() and operators.get(item) <= operators.get(opStack.top()):
                    postfixOp+=opStack.pop()
                opStack.push(item)
                
            elif item == ')':
                while opStack.top() != '(':
                    postfixOp+=opStack.pop()
                opStack.pop()
                    
            else:
                while not opStack.isEmpty():
                    postfixOp+=opStack.pop()
                postfixOp+=item
    
    return postfixOp

def evaluatePostfix(operation):
    
    opStack = stack()
    operators = ['+', '-', '*', '/']
    
    while len(operation) > 0:
        
        item = operation[0]
        operation = operation[1:]
        
        if item not in operators and item != ';':
            opStack.push(item)
        
        else:
            operand2 = opStack.pop()
            operand1 = opStack.pop()
            r = eval(f'{operand1}{item}{operand2}')
            opStack.push(r)
    
    print(opStack.top())
    return opStack.pop()

if task == 'eval':
            
    infixOp = operation[0]
    print(f'infix  :  {infixOp}')
    
    postfixOp = convertToPost(infixOp)
                                    
    print(f'postfix:  {postfixOp}')
    
    result = evaluatePostfix(postfixOp)
    
    print(f'eval   :  {result}')