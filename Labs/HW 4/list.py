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

# Create a linked list to serve as foundation for the stack
class DLinkedList():
    
    # Limit the DLinkedList class to only having head and tail attributes to conserve space
    __slots__ = ['head', 'tail']
    
    # Create a Node class to store elements of linked list
    # Nested within the linked list so that it is only accessible by the list
    class Node():
        
        # Limit the Node class to having only val, next, and prev attributes to conserve space
        __slots__ = ['val', 'next', 'prev']
        
        # Initialise a Node with value val and possible next and previous nodes
        def __init__(self, val, next = None, prev = None):
            self.val = val
            self.next = next
            self.prev = prev
    
    # Initialise an empty list
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Check if the list is empty by seeing if there if head has a value
    def isEmpty(self):
        return self.head == None
    
    # Add a new value to an empty list by setting head and tail equal to same Node
    def __addEmpty(self, val):
        self.head = self.Node(val)
        self.tail = self.head
    
    # Add a new head value to the list
    def addHead(self, val):
        
        # Check if the list is empty, if so simply use helper function to add new Node
        if self.isEmpty():
            self.__addEmpty(val)
            return
        
        # If list is not empty, create new head Node
        # The new head Node points to the former head Node as the next Node
        self.head = self.Node(val, next=self.head)
        
        # Make the former head Node point to the new head Node as its previous Node
        self.head.next.prev = self.head
    
    # Add a new tail value to the list
    def addTail(self, val):
        
        # Check if the list is empty, if so simply use helper function to add new Node
        if self.isEmpty():
            self.__addEmpty(val)
            return
        
        # If list is not empty, create new tail Node
        # The new tail Node points to the former tail Node as its previous Node
        self.tail = self.Node(val, prev=self.tail)
        
        # Make the former tail Node point to the new tail Node as its next Node
        self.tail.prev.next = self.tail        
    
    # Remove the head Node from the list
    def removeHead(self):
        
        # If the list is empty
        if self.isEmpty():
            
            # Return false to indicate the operation cannot be completed
            return False
        
        # Else if the list has only one Node
        elif self.head == self.tail:
            
            # Set head and tail of list equal to none
            self.head = None
            self.tail = None
            
            # Return true to indicate the operation has been completed
            return True
        
        # Else (the list is not empty and contains more than one Node)
        else:
            
            # Shift head to being the second Node in the list
            self.head = self.head.next
            
            # Remove the reference to the Node that was previously the head
            self.head.prev = None
            
            # Return true to indicate the operation was completed
            return True
    
    # Remove the tail Node from the list
    def removeTail(self):
        
        # If the list is empty
        if self.isEmpty():
            
            # Return false to indicate the operation cannot be completed
            return False
        
        # Else if the list has only one Node
        elif self.head == self.tail:
            
            # Set head and tail of list equal to none
            self.head = None
            self.tail = None
            
            # Return true to indicate the operation has been completed
            return True
        
        # Else (the list is not empty and contains more than one Node)
        else:
            
            # Shift tail to being penultimate Node in the List
            self.tail = self.tail.prev
            
            # Remove reference to the Node that was previously tail
            self.tail.next = None
            
            # Return true to indicate the operation has been completed
            return True
    
    # Retun the head value of the list
    def getHead(self):
        return self.head.val
    
    # Return the tail value of the list
    def getTail(self):
        return self.tail.val
    
    #  Return a string form of the list, showing each Node's value
    def __str__(self):
        node = self.head
        s = ''
        while node != None:
            s+=f'{node.val},'
            node = node.next
        return s