class List():
    __slots__ = 'head', 'tail'
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head == None
    
    def getHead(self):
        assert not self.isEmpty()
        return self.head.data
    
    def getTail(self):
        assert not self.isEmpty()
        return self.tail.data
    
    def addEmpty(self, data):
        self.head = self.Node(data)
        self.head = self.tail
        
    def addHead(self, data):
        if self.isEmpty():
            self.addEmpty(data)
            return True
        
        self.head = self.Node(data, self.head)
        
    def addTail(self, data):
        if self.isEmpty():
            self.addEmpty(data)
            return True
        
        self.tail.next = self.Node(data)
        self.tail = self.tail.next
    
    class Node():
        __slots__ = ['data', 'next']
        
        def __init__(self, data, next=None):
            self.data = data
            assert next == None or type(next) == List.Node
            self.next = next
            
class DLinkedList():
    __slots__ = ['head', 'tail']
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head == None
    
    def addEmpty(self, data):
        self.head = self.Node(data, next=None, prev=None)
        self.tail = self.head
    
    def addHead(self, data):
        if self.isEmpty():
            self.addEmpty(data)
            return
        self.head.prev = self.Node(data, next=self.head, prev=None)
        self.head = self.head.prev
    
    def addTail(self, data):
        if self.isEmpty():
            self.addEmpty(data)
            return
        self.tail.next = self.Node(data, next=None, prev=self.tail)
        self.tail = self.tail.next
        
    def hasLast(self):
        return self.head == self.tail and not self.isEmpty()
    
    def removeLast(self):
        assert self.hasLast()
        self.head = None
        self.tail = None
        
    def removeHead(self):
        self.head = self.head.next
        self.head.prev = None
    
    def removeTail(self):
        self.tail = self.tail.prev
        self.tail.next = None
    
    def __str__(self):
        i = self.head
        temp = ''
        while i != None:
            temp+=f"{(i.data, i.prev.data if i.prev != None else None, i.next.data if i.next != None else None)} -> "
            i = i.next
        return temp
    
    class Node():
        __slots__ = ['data', 'next', 'prev']
        
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

a = DLinkedList()
a.addHead(1)
a.addTail(2)
a.addTail(3)
a.addTail(4)
print(a)