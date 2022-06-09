# This is my simple binary_search_tree implementation

# Blueprint to a single node, sub-class of BST
class Node:

    def __init__(self, key, data=None, left=None, right=None, parent=None):
        # A key identifies a node and is needed for insert logic
        self.key = key
        # and some sort of data
        self.data = data
        # and a reference to its child_nodes (in this case binary: l/r)
        self.left = left
        self.right = right
        # A reference to the parent node
        self.parent = parent

    def __repr__(self):
        # Returns a presentable print instead of default printable
        return 'Object with key: ' + str(self.key) + ' and data: ' + str(self.data)

# Blueprint to a BST
class BinarySearchTree:

    def __init__(self):
        # A tree has atleast a root
        self.root = None

    ### MAIN METHODS OF A BST ###

    # Insertion 
    def bst_insert(self, new_node):
        # Key
        key = new_node.key
        # Start with
        node = self.root
        # Check if tree is empty
        if node is None:
            # Insert root
            self.root = new_node
            # and terminate the function
            return
        # Find appropriate parent for new_node
        while node is not None:
            parent = node
            # Check if node is already in the tree
            if node.key == key:
                print('Node is already in the tree!')
                # and terminate the function
                return
            # If node key is larger than new_node key
            elif node.key > key:
                # walk left
                node = node.left
            # If node key is smaller than new_node key
            elif node.key < key:
                # walk right
                node = node.right
        # One parent has been found insert node accordingly
        if parent.key > key:
            parent.left = new_node
        else:
            parent.right = new_node
        # Tell new_node about its parent
        new_node.parent = parent

    # Search - iterative implementation
    def bst_search_iter(self, key):
        # Start with root node
        node = self.root
        # While tree is empty and key has not been found 
        while node is not None and node.key != key:
            # If key is smaller walk left
            if node.key > key:
                node = node.left
            # If key is larger walk right
            elif node.key < key:
                node = node.right
        # At the end return the node
        return node
 
    # Deletion
    # Case 1: Node is a leaf node
    # Case 2: Node has one child.
    # Case 3: Node has 2 children  
    def bst_delete(self, node):
        ...

    # Helper function to delete a leaf-node
    def _delete_leaf(self, node):
        ...
    # Helper function to shift nodes in a tree
    def _shift_nodes(self, node):
        ...

    ### ADDITIONAL COOL METHODS OF A BST ###

    # Traversal
    def in_order_traversal(self, node):
        # Check if tree is empty first 
        if node is not None:
            # Recursive call left sided nodes
            self.in_order_traversal(node.left)
            # Print the node (or use() method)
            print(node)
            # Recursive call right sided nodes
            self.in_order_traversal(node.right)

    # Successor/Predecessor
    def bst_successor(self, node):
        if node.right is not None:
            return self.bst_minimum(node.right)
        parent = node.parent
        while parent is not None and node == parent.right:
            node = node.parent
            parent = node.parent.parent
        return parent

    def bst_predecessor(self, node):
        if node.left is not None:
            return self.bst_maximum(node.left)
        parent = node.parent
        while parent is not None and node == parent.left:
            node = node.parent
            parent = node.parent.parent
        return parent

    # Min/Max
    def bst_maximum(self, node):
        node = self.root
        while node.right is not None:
            node = node.right
        return(node)

    def bst_minimum(self, node):
        node = self.root
        while node.left is not None:
            node = node.left
        return(node)