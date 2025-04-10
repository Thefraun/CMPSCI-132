from list import DLinkedList as linkedList

class Stack():
    
    __slots__ = ['lst']
    
    def __init__(self):
        self.lst = linkedList()
    
    def isEmpty(self):
        return self.lst.isEmpty()
    
    def push(self, val):
        self.lst.addHead(val)
    
    def pop(self):
        popped = self.lst.getHead()
        self.lst.removeHead()
        return popped
    
    def clear(self):
        self.lst.head = None
        self.lst.tail = None
    
    def top(self):
        return self.lst.getHead()