# Inverting Binary tree means nothing but finding the mirror image of the binary tree
from BinaryTree import binaryTreeMethods

def invertTree(root):
    if root == None or root.left == None and root.right == None:
        return
    leftChild = root.left
    root.left = root.right
    root.right = leftChild
    invertTree(root.left)
    invertTree(root.right)
    return root

bt = binaryTreeMethods()
root = bt.inputLevelWise()
bt.printLevelWise(root)
print("---------------------------------")
root =invertTree(root)
bt.printLevelWise(root)

