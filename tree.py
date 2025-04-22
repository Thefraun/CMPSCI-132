class Tree():
    
    __slots__ = ['root']
    
    class Node():
        
        __slots__ = ['val', 'left', 'right']
        def __init__(self, v, l=None, r=None):
            self.val = v
            self.left = l
            self.right = r
            
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None
    
    def addNode(self, v):
        if self.isEmpty():
            self.root = self.Node(v)
        else:
            self._addNode(v, self.root)
    
    def _addNode(self, v, current):
        if v > current.val:
            if current.left == None:
                current.left = self.Node(v)
            else:
                self._addNode(v, current.left)
        elif v < current.val:
            if current.right == None:
                current.right = self.Node(v)
            else:
                self._addNode(v, current.right)
    
    def buildTree(self):
        self.root = self.Node(1, self.Node(11), self.Node(9))
        self.root.left.left = self.Node(14)
        self.root.left.right = self.Node(5, l=self.Node(20))
        self.root.right.left = self.Node(21)

    def printInPreorder(self):
        self._printInPreorder(self.root)
    
    def _printInPreorder(self, current):
        if current == None:
            return
        print(f'{current.val}, ', end='')
        self._printInPreorder(current.left)
        self._printInPreorder(current.right)
        
    def printInPostorder(self):
        self._printInPostorder(self.root)
    
    def _printInPostorder(self, current):
        if current == None:
            return
        self._printInPostorder(current.left)
        self._printInPostorder(current.right)
        print(f'{current.val},', end='')
    
    def printInorder(self):
        self._printInorder(self.root)
    
    def _printInorder(self, current):
        if current == None:
            return
        self._printInorder(current.left)
        print(f'{current.val},', end='')
        self._printInorder(current.right)
    
    def printBreadthFirst():
        pass

t = Tree()
t.buildTree()
t.printInorder()