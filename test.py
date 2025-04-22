
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)
        return node
    
    def findMin(self):
        if self.root is None:
            raise ValueError("Tree is empty")
        return self._find_min_recursive(self.root)

    def _find_min_recursive(self, node):
        if node is None:
            return float('-inf')  # Identity for min comparison

        left_min = self._find_min_recursive(node.left)
        right_min = self._find_min_recursive(node.right)

        print(f'Current: {node.key}, leftMin: {left_min}, rightMin: {right_min}')
        return max(node.key, left_min, right_min)

        
# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(30)

    # When `findMin` is implemented:
    print(f"Minimum value is {bst.findMin()}")