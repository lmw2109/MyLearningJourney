# This is my Adelson-Velsky and Landis (AVL) tree implementation
# Any uncommented code is most-likely explained in my simple implementation
# of a Binary Search Tree: see 'bst.py'

from math import log, log2, sqrt

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
            # utilizing the additional information methods below
            # print('Height is: ' + str(self.height(self.root)))
            # print('Nodes: ' + str(self.count(self.root)))
            # self.height_interval()

    # Balance factor helper function
    def _cal_bf(self, node):
        # bf = height(r-subtree) - height(l-subtree)
        balance_factor = self.height(node.right) - self.height(node.left)
        # update node with its balance factor
        node.bf = balance_factor
        # optionally returns it
        return balance_factor

    # Retraces path to scan if tree is unbalanced
    def _retrace(self, node):
        # current is passed parameter (inserted node or parent of deleted node)
        cur = node
        # Check if cur is unbalanced (happens with deletion)
        self._cal_bf(cur)
        # if cur is a left-heavy breakpoint return it and its left child
        if (cur.bf == -2):
            return [cur.left, cur]
        # if cur is a right-heavy breakpoint return it and its right child
        if (cur.bf == 2):
            return [cur.right, cur]
        # Otherwise continue with path upwards (retraceing begins here)
        # while path upwards has not reached root
        while cur.parent is not None:
            # calculate parents balance factor
            self._cal_bf(cur.parent)
            # if cur is a left-heavy breakpoint return it and its left child
            if (cur.parent.bf == -2):
                return [cur.parent.left, cur.parent]
            # else if cur is a right-heavy breakpoint return it and its right child
            elif (cur.parent.bf == 2):
                return [cur.parent.right, cur.parent]
            # take a step and repeat
            cur = cur.parent
        # Return if no node in range (-2, 2) was found
        return

    ### MAIN METHODS ###

    # Search
    def search_iter(self, key):
        node = self.root
        while node is not None and node.key != key:
            if node.key > key:
                node = node.left
            elif node.key < key:
                node = node.right
        if node is None:
            return ('No such node was found!')
        return node

    # Insert
    # -> Dynamic change: requires rebalancing
    def avl_insert(self, new_node):
        # standard insertion procedure
        key = new_node.key
        node = self.root
        if node is None:
            self.root = new_node
            self.root.bf = 0
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
        # insert always as leaf: bf = 0
        new_node.bf = 0
        # update bf values and rotate if necessary
        self._rotation_decision(new_node)

    # Delete
    # -> Dynamic change: requires rebalancing
    def avl_delete(self, node):
        # standard deletion procedure
        if not (node.left and node.right):
            self._shift_nodes(node)
        else:
            pred = node.left
            while pred.right is not None:
                pred = pred.right
            node.key = pred.key
            node.data = pred.data
            self._shift_nodes(pred)
        # update bf values and rotate if necessary
        self._rotation_decision(node)

    # Helper function to handle deletion and substitution
    def _shift_nodes(self, node):
        # cache parent for retracing after operation
        parent = node.parent
        # standard deletion procedure
        child_node = node.left or node.right
        if node.parent:
            if node.parent.left == node:
                node.parent.left = child_node
            else:
                node.parent.right = child_node
            if child_node:
                child_node.parent = node.parent
        else:
            self.root = child_node
            child_node.parent = None
        # update bf values and rotate if necessary
        self._rotation_decision(parent)   

    ### NODE ROTATION METHODS ###

    # Handles the decision logic for rotations
    def _rotation_decision(self, node):
        # retrace and find breakpoint
        nodes = self._retrace(node)
        # In case there is no breakpoint return
        if nodes == None:
            return
        # nodes of interest
        x = nodes[0] # child of unbalance node
        u = nodes[1] # unbalanced node range(-2; 2)
        # rotation right in deletion case [0, -2]
        if (x.bf == 0 and u.bf == -2):
            self._rotate_right(x, u)
            # update balance factors
            x.bf += 1
            u.bf += 1
            return
        # rotation left in deletion case [0, 2]
        elif (x.bf == 0 and u.bf == 2):
            self._rotate_left(x, u)
            # update balance factors
            x.bf += -1
            u.bf += -1
            return
        # rotation right if [-1,-2]
        elif (x.bf == -1 and u.bf == -2):
            self._rotate_right(x, u)
            # update balance factors
            x.bf = 0
            u.bf = 0
            return
        # rotation left if [1,2]
        elif (x.bf == 1 and u.bf == 2):
            self._rotate_left(x, u)
            # update balance factors
            x.bf = 0
            u.bf = 0
            return
        # rotation right_left if [-1,2]
        elif (x.bf == -1 and u.bf == 2):
            self._rotate_right_left(x, u)
            # update balance factors
            self._cal_bf(x)
            u.bf = 0
            x.parent.bf = 0
            return
        # rotation left_right if [1,-2]
        elif (x.bf == 1 and u.bf == -2):
            self._rotate_left_right(x, u)
            # update balance factors
            self._cal_bf(x)
            u.bf = 0
            x.parent.bf = 0
            return
        # Else there must be an error!
        else:
            print('Error: set of balance factors not recognized!')

    # Simple Rotations #

    def _rotate_left(self, x, u):
        # 'right-right situation'
        # cache nodes that are needed for the operation
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
        if u is self.root:
            # update the root
            self.root = x
            x.parent = None

    def _rotate_right(self, x, u):
        # 'left-left situation'
        # cache nodes that are needed for the operation
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
        if u is self.root:
            # update the root
            self.root = x
            x.parent = None

    # Double Rotations #

    # Subtree of right-heavy tree is left-heavy
    def _rotate_right_left(self, x, u):
        # y in this case is x's left child
        y = x.left
        # first rotate left heavy-tree to be right-heavy
        self._rotate_right(y, x)
        # now a left rotation of the tree also balances the subtree
        self._rotate_left(y, u)

    # Subtree of left-heavy tree is right-heavy
    def _rotate_left_right(self, x, u):
        # y in this case is x's right child
        y = x.right
        # first rotate right heavy-tree to be left-heavy
        self._rotate_left(y, x)
        # now a right rotation of the tree also balances the subtree
        self._rotate_right(y, u)

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

    # Returns a report of the height-interval of an AVL-Tree at n nodes
    def height_interval(self):
        # N nodes in the tree
        n = self.count(self.root)

        # Calculation min_height
        lower = log2(n+1)
        # Calculation max_height
        upper = 1.4405*log2(n+2)-0.3277

        print('For an AVL-Tree of '+ str(n) +' nodes the height lies in between')
        print(str(lower) + ' and ' +  str(upper))

    # Count
    def count(self, node):
        if self.root is None:
            return 0
        count = 1
        if node.left:
            count += self.count(node.left)
        if node.right:
            count += self.count(node.right)
        return count

    # Report
    def report(self):
        print('Root: ' + str(self.root))
        print('Height is: ' + str(self.height(self.root)))
        print('Nodes: ' + str(self.count(self.root)))
        self.height_interval()
