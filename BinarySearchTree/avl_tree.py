# This is my Adelson-Velsky and Landis (AVL) tree implementation
# Any uncommented code is most-likely explained in my simple implementation
# of a Binary Search Tree: see 'bst.py'

class Node:

    def __init__(self, key, data=None, left=None, right=None, parent=None, bf=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        # The balance factor will determine the type of rotation that is needed to keep the tree balanced!
        self.bf = bf

    def visualize(self, level):
        result = " "*4*level + f"{self.key}: {self.bf}"
        if self.left: result =  self.left.visualize(level + 1) + "\n" + result
        if self.right: result += "\n" + self.right.visualize(level + 1)            
        return result

    def __repr__(self):
        return 'Object with key: ' + str(self.key) + ' and BF: ' + str(self.bf)

class AdelsonVelskyLandis():

    def __init__(self):
        self.root = None

    def visualize(self):
        if self.root:
            print(self.root.visualize(0))

    ### MAIN METHODS ###

    # Search
    def search_iter(self, key):
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

    # Balance factor helper function
    def _cal_bf(self, node):
        # bf = height(r-subtree) - height(l-subtree)
        balance_factor = self.height(node.right) - self.height(node.left)
        # update node with its balance factor
        node.bf = balance_factor

    # Simple Rotations #

    def _rotate_left(self, y):
        # y is the right child of the right node we have to rotate around
        # 'right-right situation'
        # cache nodes that are needed for the operation
        x = y.parent
        u = x.parent
        z = x.left
        p = u.parent
        # new parent of z
        if z: # only if there is a node z
            z.parent = u
        # new parent of x
        x.parent = p
        # new parent of u
        u.parent = x
        # new child of p is x
        if p:
            # find out if u is left or right child and insert x into that position
            if u is p.left:
                p.left = x
            else:
                p.right = x
        # new right child of u is z
        u.right = z
        # new left child of x is u
        x.left = u
        # if root of tree has been involved
        if x.parent is None:
            # update the root
            self.root = x
        # recalculate balance factors
        self._cal_bf(u)
        self._cal_bf(x)
        self._cal_bf(y)

    def _rotate_right(self, y):
        # y is the left child of the left node we have to rotate around
        # 'left-left situation'
        # cache nodes that are needed for the operation
        x = y.parent
        u = x.parent
        z = x.right
        p = u.parent
        # new parent of z
        if z: # only if there is a node z
            z.parent = u
        # new parent of x
        x.parent = p
        # new parent of u
        u.parent = x
        # new child of p is x
        if p:
            # find out if u is left or right child and insert x into that position
            if u is p.left:
                p.left = x
            else:
                p.right = x
        # new left child of u is z
        u.left = z
        # new right child of x is u
        x.right = u
        # if root of tree has been involved
        if x.parent is None:
            # update the root
            self.root = x
        # recalculate balance factors
        self._cal_bf(u)
        self._cal_bf(x)
        self._cal_bf(y)

    # Double Rotations #

    def _rotate_right_left():
        ...

    def _rotate_left_right():
        ...

    ### ADDITIONAL FUNCTIONS ###

    # Traversal
    def in_order_traversal(self, node): 
        if node is not None:
            self.in_order_traversal(node.left)
            print(node)
            self.in_order_traversal(node.right)

    # Min/Max
    def maximum(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return(node)

    def minimum(self):
        node = self.root
        while node.left is not None:
            node = node.left
        return(node)

    # Height
    def height(self, node):
        if node:
            return max(self.height(node.left), self.height(node.right)) + 1
        else:
            return 0
    
    # Count
    def count(self, node):
        if self.root is None:
            return 0
        count = 1
        if node.left:
            count += self.bst_count(node.left)
        if node.right:
            count += self.bst_count(node.right)
        return count

    # TEMPORARY FOR TESTS

    # Insertion 
    def insert(self, new_node):
        key = new_node.key
        node = self.root
        if node is None:
            self.root = new_node
            return
        while node is not None:
            parent = node
            if node.key == key:
                print('Node is already in the tree!')
                return
            elif node.key > key:
                node = node.left
            elif node.key < key:
                node = node.right
        if parent.key > key:
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.parent = parent