#---------------------------------------------------------------------
# Name: Logan Fraunfelter
# Email: lsf5185@psu.edu
# Class: CMPSC 132
# Program 1.4 / HW 4
# Due Date: April 10, 2025
#
# Description: This program accepts command line arguments specifying
# whether to perform linked list operations or conversion and
# evaluation of an operation, given in infix notation, and performs
# the required operations.
#
# Acknowledgement:
# I based my implementation of infix to postfix conversion and
# evaluation of a postfix operation on the algorithm provided in
# the class notes.
#---------------------------------------------------------------------

from list import DLinkedList
from stack import Stack
import sys

# A function to return the precendence of each operator to determine where/when it is placed in the stack
def getPrecendence(item):
    
    if item == '*' or item == '/':
        return 2
    
    elif item == '+' or item == '-':
        return 1
    
    elif item == '(' or item == ')':
        return 0
    
    else:
        return -1

# Function to convert infix notation operation to postfix notation operation
def convertToPost(operation):
    
    postfixOp = ''
    opStack = Stack()

    # Loop through each item in the operation
    while len(operation) > 0:
        
        # Get the first item, and then remove it from the operation
        item = operation[0]
        operation = operation[1:]
        
        # If the item is a number, add it to the final resulting operation
        if item != ';' and getPrecendence(item) == -1:
            postfixOp+=item
        
        # If the item is not a number
        else:
            
            # If it is an (, push it to the stack
            if item == '(':
                opStack.push(item)
            
            # Else if it is a ), pop each item in the stack until the matching ( is found
            elif item == ')':
                
                while opStack.top() != '(':
                    
                    # Store each popped item in the final operation
                    postfixOp+=opStack.pop()
                
                # Remove the ( from the stack
                opStack.pop()
            
            # Else if it is an operator that is neither ( or )
            elif getPrecendence(item) > 0:
                
                # While the stack is not empty and the precedence of the current item is lower than the item at the top of the stack
                while not opStack.isEmpty() and getPrecendence(item) <= getPrecendence(opStack.top()):
                    
                    # Pop the top of the stack and store it in the resulting operation
                    postfixOp+=opStack.pop()
                
                # Push the current item to the top of the stack
                opStack.push(item)
            
            # Else (the item is a ;)
            else:
                
                # Pop every item in the stack and add it to the final operation
                while not opStack.isEmpty():
                    
                    postfixOp+=opStack.pop()
                
                # Add the ; to the final operation
                postfixOp+=item
    
    # Return the final operation, now in postfix notation
    return postfixOp

# Function to evaluate a postfix operation and return the result
def evaluatePostfix(operation):
    
    opStack = Stack()
    operators = ['+', '-', '*', '/']
    
    # Loop through the given operation (excluding the final semicolon)
    while len(operation) - 1 > 0:
        
        # Get the first item in the operation
        item = operation[0]
        
        # Remove the first item from the operation, preserving the rest of the operation
        operation = operation[1:]
        
        # If the item is a number, put it in the stack
        if item not in operators:
            opStack.push(item)
        
        # If the item is an operation, pop the top two numbers in the stack and perform the operation
        else:
            operand2 = opStack.pop()
            operand1 = opStack.pop()
            r = eval(f'{operand1}{item}{operand2}')
            
            # Push the result of the operation into the stack
            opStack.push(r)
    
    # Return the final resulting number in the stack
    return opStack.pop()

# Get what task should be performed (eval or linked-list)
task = sys.argv[1]

# Get the specific operations to be performed
operations = sys.argv[2:]

if task == 'eval':
    
    # Store and print the original infix operation
    infixOp = operations[0]
    print(f'infix  :  {infixOp}')
    
    # Convert the infix operation to postfix and print
    postfixOp = convertToPost(infixOp)      
    print(f'postfix:  {postfixOp}')
    
    # Evaluate the result of the postfix operation and print
    result = evaluatePostfix(postfixOp)
    print(f'eval   :  {result}')

else:
    
    # Create an empty linked list to perform list operations
    lst = DLinkedList()
    
    # Loop through each given list command, and perform the associated operation
    for operation in operations:
        operation = operation.lower()
        
        if operation.find('addtohead') != -1:
            lst.addHead(operation[operation.find(':') + 1:])
            
        elif operation.find('addtotail') != -1:
            lst.addTail(operation[operation.find(':') + 1:])
            
        elif operation.find('removehead') != -1:
            lst.removeHead()
        
        elif operation.find('removetail') != -1:
            lst.removeTail()
    
    # Print the resulting list
    print(lst)