from BinaryTree import binaryTreeMethods

def isSameTree(node1, node2):
    if node1 == None and node2 == None:
        return True
    if node1 == None or node2 == None:
        return False
    
    # check is subroot is a subtree of the current root
    return (node1.val == node2.val) and isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right)
def isSubtree(root, subRoot):
    if root == None and subRoot == None:
        return True
    if root == None  or subRoot == None:
        return False
    return isSameTree(root, subRoot) or isSameTree(root.left, subRoot) or isSameTree(root.right,subRoot)


bt1 = binaryTreeMethods()
bt2 = binaryTreeMethods()
root = bt1.inputLevelWise()
subRoot = bt2.inputLevelWise()
print(isSubtree(root, subRoot))
