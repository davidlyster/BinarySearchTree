import random

"""
NOTE
This is just being done with Node values for simplification (no keys)
https://en.wikipedia.org/wiki/Binary_search_tree

Better for lookup than normal list/array as instead of searching 1by1 for a value/key,
useless stems of the tree will be ignored and not traversed saving time

Algorithm		Average	    Worst case
Space		    O(n)	    O(n)
Search		    O(log n)	O(n)
Insert		    O(log n)	O(n)
Delete		    O(log n)	O(n)
"""


class Node:
    """
    Each node has a value and its left and right child (if they exist) will have a value
    less than or greater than the nodes values respectively
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.depth = 0

    def insert(self, value):
        if not self.root:
            # if no root exists, insert the value (as a new Node) as the root
            self.root = Node(value)
        else:
            # otherwise, the tree exists, so move into the private recursive function
            # the recursion will start at the root node but this will be replaced by the node currently being
            # 'examined' in the recursive function call when traversing the tree
            self._insert(value, self.root, 0)

    def _insert(self, value, node, depth):
        """
        Private ("_"insert()) function used to recursively traverse the tree and insert the value in its correct pos

        CHECKS:
        - does the current value exist in tree? if so do nothing (maybe print something)
            - if we were checking by keys instead, if the key existed, we would simply update the node value

        - if value is less that the current nodes value - WE GO LEFT
            - if there is no left child, insert a new node (left) with value
            - if there is a left child, recurse again (down the tree)

        - if value is greater that the current nodes value - WE GO RIGHT
            - if there is no right child, insert a new node (right) with value
            - if there is a right child, recurse again (down the tree)
        """

        if value < node.value:
            if node.left:
                self._insert(value, node.left, depth+1)
            else:
                node.left = Node(value)
                # depth is +1 because of new node
                # mark that as tree depth if it is now the longest stem
                if depth+1 > self.depth:
                    self._increase_depth(depth+1)

        elif value > node.value:
            if node.right:
                self._insert(value, node.right, depth+1)
            else:
                node.right = Node(value)
                # depth is +1 because of new node
                # mark that as tree depth if it is now the longest stem
                if depth+1 > self.depth:
                    self._increase_depth(depth+1)

        else:
            print("Value already exists in tree {0}".format(value))

    def _increase_depth(self, new_depth):
        self.depth = new_depth

    def print_tree(self):
        # if there is a root, go into the recursive private function to begin printing tree
        # printing depth (0 here) is included so as to print what depth a particular node is at
        # this way you could use the depth counter to build/imagine/view the tree
        if self.root:
            print("ROOT: {0}".format(self.root.value))
            self._print_tree(self.root, 0)

    def _print_tree(self, node, printing_depth):
        """
        If a given node exists in the tree:

        - recurse down the left of the tree printing everything following this recursive call/pattern
        - then print this node('s values)
        - then recurse down the right too
        """
        if node:
            self._print_tree(node.left, printing_depth+1)       # LEFT
            print(str(node.value)+"\t\t"+str(printing_depth))   # THIS
            self._print_tree(node.right, printing_depth+1)      # RIGHT

    # I've actually replaced the need for these by adding 'depth' to the print tree and insert functions
    # useful as a way to track the depth/height if the depth was not tracked anywhere else though
    def get_height(self):
        """
        function to get depth of tree using private _get_height() recursive function
        """
        if self.root:
            return self._get_height(self.root, 0)
        else:
            return 0

    def _get_height(self, node, current_height):
        """
        works by getting the height of all trees and returning the max of them
        """
        if node is None:
            return current_height

        left_height = self._get_height(node.left, current_height+1)
        right_height = self._get_height(node.right, current_height+1)

        return max(left_height, right_height)


def run(list_of_values):
    """
    function to run program
    """

    print("Values List Length: {0}".format(len(list_of_values)))  # 50 by default
    print("Values: {0}".format(str(list_of_values)))              # unordered list
    print()

    # create the tree object
    bst = BinarySearchTree()

    # insert values into tree
    for val in list_of_values:
        bst.insert(val)

    print()
    print("Values inserted")
    print()

    bst.print_tree()

    print()
    print("Tree Depth: {0}".format(bst.depth))
    print()


"""
RUN PROGRAM
- fill in values and click run
- the randomiser will be used by default but users can put in their own array if they want to simulate their own tree
"""

# produce 100 random numbers (with duplicates)
values = [random.randint(1, 100) for each in range(50)]
# values = [40,12,5,40,4,6,45,76,72,93]     # put in manual stuff if you want

run(values)         # values should now be output in order