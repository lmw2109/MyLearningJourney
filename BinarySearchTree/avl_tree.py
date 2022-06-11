# This is my Adelson-Velsky and Landis (AVL) tree implementation
# Any uncommented code is most-likely explained in my simple implementation
# of a Binary Search Tree: see 'bst.py'

class Node:

    def __init__(self, key, data=None, left=None, right=None, parent=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def visualize(self, level):
        result = " "*4*level + f"{self.key}: {self.data}"
        if self.left: result =  self.left.visualize(level + 1) + "\n" + result
        if self.right: result += "\n" + self.right.visualize(level + 1)            
        return result

    def __repr__(self):
        return 'Object with key: ' + str(self.key) + ' and data: ' + str(self.data)

class AdelsonVelskyLandis():

    def __init__(self):
        self.root = None

    def visualize(self):
        if self.root:
            print(self.root.visualize(0))

    ### MAIN METHODS ###

    # Search
    # -> Read only operation: like basic bst
    def avl_search_iter(self, key):
        node = self.root
        while node is not None and node.key != key:
            if node.key > key:
                node = node.left
            elif node.key < key:
                node = node.right
        return node

    # Insert
    # -> Dynamic change: requires rebalancing
    def avl_insert():
        ...

    # Delete
    # -> Dynamic change: requires rebalancing
    def avl_delete():
        ...

    ### NODE ROTATION METHODS ###

    # Simple Rotations #

    def _right_right():
        ...
    
    def _left_left():
        ...

    # Double Rotations #

    def _right_left():
        ...

    def _left_right():
        ...

    ### ADDITIONAL FUNCTIONS ###

    # Traversal
    # -> like basic bst
    def in_order_traversal(self, node): 
        if node is not None:
            self.in_order_traversal(node.left)
            print(node)
            self.in_order_traversal(node.right)

    # Min/Max
    # -> like basic bst
    def bst_maximum(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return(node)

    def bst_minimum(self):
        node = self.root
        while node.left is not None:
            node = node.left
        return(node)

    # Height
    # -> like basic bst
    def bst_height(self, node):
        if node:
            return max(self.bst_height(node.left), self.bst_height(node.right)) + 1
        else:
            return 0
    
    # Count
    # -> like basic bst
    def bst_count(self, node):
        if self.root is None:
            return 0
        count = 1
        if node.left:
            count += self.bst_count(node.left)
        if node.right:
            count += self.bst_count(node.right)
        return count