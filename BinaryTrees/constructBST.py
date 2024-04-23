from BinaryTree import binaryTree, binaryTreeNode

def constructBST(lst):
    if len(lst)==0:
        return
    mid = -1
    if len(lst)%2==0:
        mid = (len(lst)//2)-1
    else:
        mid = len(lst)//2

    rootNode = binaryTreeNode(lst[mid])
    leftTree = constructBST(lst[0:mid])
    rightTree = constructBST(lst[mid+1:])

    rootNode.left = leftTree
    rootNode.right = rightTree
    return rootNode


lst = [int(ele) for ele in input().split()]
root = constructBST(lst)
bt = binaryTree()
bt.levelWiseTreePrintHelper(root)

