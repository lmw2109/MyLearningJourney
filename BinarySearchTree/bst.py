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

    def visualize(self, level):
        result = " "*4*level + f"{self.key}: {self.data}"
        if self.left: result =  self.left.visualize(level + 1) + "\n" + result
        if self.right: result += "\n" + self.right.visualize(level + 1)            
        return result

    def __repr__(self):
        # Returns a presentable print instead of default printable
        return 'Object with key: ' + str(self.key) + ' and data: ' + str(self.data)

# Blueprint to a BST
class BinarySearchTree:

    def __init__(self):
        # A tree has atleast a root
        self.root = None

    def visualize(self):
        if self.root:
            print(self.root.visualize(0))

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
        # Once parent has been found insert node accordingly
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
        # Check if node has less than 2 children
        if not (node.left and node.right):
            # If so call helper function to deal with cases 1 and 2
            self._shift_nodes(node)
        # Else we've got a case 3 on our hands!
        else:
            # Find predecessor
            pred = node.left
            while pred.right is not None:
                pred = pred.right
            # and overwrite the node to be deleted with it
            node.key = pred.key
            node.data = pred.data
            # and remove predecessor from its previous location
            self._shift_nodes(pred)

    # Helper function to handle deletion and substitution
    def _shift_nodes(self, node):
        # Only one child so either l/r
        child_node = node.left or node.right
        # If node is not root of the tree
        if node.parent:
            # Check if node is a left node
            if node.parent.left == node:
                # and pull up child node to replace it
                node.parent.left = child_node
            else:
                # else node must be right node
                node.parent.right = child_node
        else:
            # Else node must be root
            self.root = child_node
        # Remove parent pointer
        node.parent = None

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

    # Min/Max
    def bst_maximum(self):
        # Start at the root
        node = self.root
        # Loop to retrieve the right-most leaf
        while node.right is not None:
            node = node.right
        return(node)

    def bst_minimum(self):
        # Start at the root
        node = self.root
        # Loop tp retrieve the left-most leaf
        while node.left is not None:
            node = node.left
        return(node)