"""
Implementation of inOrder traversal of a tree
The traversal is implemented iteratively with
the help of a Morris traversal

The traversal works in O(n) time and O(1) space
"""

# Making the file look into it's parent folder's subdirectories
# for modules using sys.path
import sys
sys.path.append('../')

# Importing the already created code for tree creation
# This lets us focus on the specific task in this file
# Check folder with the module name in the parent folder
import TreeCreation.SimpleBinaryTree as SBT

"""
InOrder Traversal through Morris traversal
"""
def InOrderByMorris(root):

    # Initialize a pointer to the root of tree
    curr = root

    # Iterating through the tree
    while curr :

        # if left child of current node does not exist
        if not curr.left:

            # Simply visit the node and move to right
            print(curr.data, end = " ")

            curr = curr.right

        else:

            # Calculate the predecessor of the current node
            # It is the rightmost node of the left subtree of current
            pred = curr.left

            while pred.right and pred.right != curr:

                pred = pred.right

            # If the predecessor's right is NULL
            # Make current as it's right child and move left
            if not pred.right:

                pred.right = curr

                curr = curr.left

            # If predecessor's right has the current node
            # Means we have visited its left subtree already
            # Nullify predecessor's right, visit the node and move right
            else:

                pred.right = None

                print(curr.data, end = " ")

                curr = curr.right

    # Simply printing the nextLine for output looks
    print()

# The driver code
if __name__ == "__main__":

    # Creating the simple Binary Tree
    root = SBT.BinaryTree()

    # Calling function to traverse inOrder iterativey using stack
    InOrderByMorris(root)
