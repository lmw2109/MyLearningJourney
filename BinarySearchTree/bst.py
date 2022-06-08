# This is a simple binary_search_tree implementation

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
        # optional: a reference to the parent node
        self.parent = parent

    def __repr__(self):
        # Returns a presentable print instead of default printable
        return 'Object with key: ' + str(self.data)

# Blueprint to a BST
class BinarySearchTree:

    def __init__(self):
        # A tree has atleast a root
        self.root = None

    ### MAIN METHODS OF A BST ###

    # Insertion
    def bst_insert(self, new_node):
        # key of new_node
        key = new_node.key
        # starting node to be investigated
        node = self.root
        # If there is nodes in the tree:
        while node is not None:
            parent = node
            # Check if key of node is equal to key of new_node
            if node.key == key:
                print('Node is already in the tree!')
            # Check if key of node is larger than key of new_node
            elif node.key > key:
                # if so: walk left in the tree
                node = node.left
            # Check if key of node is smaller than key of new_node
            elif node.key < key:
                # if so: walk right in the tree
                node = node.right
        # If there is no nodes in the tree:
        if parent is None:
            # Insert node into root
            self.root = new_node
        # If key of parent is larger than key of new_node
        elif parent.key > key:
            # insert new_node as left child
            parent.left = new_node
        # If key of parent is smaller than key of new_node
        elif parent.key < key:
            # insert new_node as right child
            parent.right = new_node
        # Tell new_node about its parent
        new_node.parent = parent

    # Search

    # Deletion

    ### ADDITIONAL COOL METHODS OF A BST ###

    # Traversal

    # Min/Max

    # Reassigning