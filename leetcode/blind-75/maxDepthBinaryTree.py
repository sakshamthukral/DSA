from BinaryTree import binaryTreeMethods

def maxDepth(root):
    if root == None:
        return 0
    leftDepth = maxDepth(root.left)
    rightDepth = maxDepth(root.right)
    return 1+max(leftDepth, rightDepth)

bt = binaryTreeMethods()
root = bt.inputLevelWise()
# bt.printLevelWise(root)
print(maxDepth(root))