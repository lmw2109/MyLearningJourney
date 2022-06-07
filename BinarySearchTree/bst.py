# This is a simple binary_search_tree implementation

# Blueprint to a single node, sub-class of BST
class Node:

    def __init__(self, data=None, left_child=None, right_child=None):
        # A node carries some sort of data or key
        self.data = data
        # and a reference to its child_nodes (in this case binary: l/r)
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self):
        # Returns a presentable print instead of default printable
        return 'Object with key: ' + str(self.data)

# Blueprint to a BST
class BinarySearchTree:

    def __init__(self):
        # A tree has atleast a root
        self.root = None

# METHODS OF A BST

    # Insertion

    # Traversal

    # Deletion

    