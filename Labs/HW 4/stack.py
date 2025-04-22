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

class Stack():
    
    # Limit the class to having only a linked list attribute
    __slots__ = ['lst']
    
    # Initialise an empty stack utilising a doubly linked list
    def __init__(self):
        self.lst = DLinkedList()
    
    # Check if the stack is empty
    def isEmpty(self):
        return self.lst.isEmpty()
    
    # Add an item to the top of the stack
    def push(self, val):
        self.lst.addHead(val)
    
    # Remove and return the top item of the stack
    def pop(self):
        popped = self.lst.getHead()
        self.lst.removeHead()
        return popped
    
    # Clear the stack
    def clear(self):
        self.lst.head = None
        self.lst.tail = None
    
    # Return the top of the stack without removing
    def top(self):
        return self.lst.getHead()