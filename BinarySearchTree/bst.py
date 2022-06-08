# This is a simple binary_search_tree implementation

# Blueprint to a single node, sub-class of BST
class Node:

    def __init__(self, data=None, left=None, right=None, parent=None):
        # A node carries some sort of data or key
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
        data = new_node.data
        node = self.root

    # Search

    # Deletion

    ### ADDITIONAL COOL METHODS OF A BST ###

    # Traversal

    # Min/Max

    # Reassigning