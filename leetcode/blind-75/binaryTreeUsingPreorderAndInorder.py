from typing import List
from BinaryTree import binaryTreeMethods, TreeNode
def buildTree(preorder,inorder):
    if len(preorder) == 0:
        return
    
    rootData = preorder[0]
    rootNode = TreeNode(rootData)
    rootIndexInorder = -1
    for j in range(len(inorder)):
        if inorder[j] == rootData:
            rootIndexInorder = j
            break
    if rootIndexInorder == -1:
        return None
    leftInorder = inorder[0:rootIndexInorder]
    rightInorder = inorder[rootIndexInorder+1:]
    lenLeftSubtree = len(leftInorder)

    leftPreOrder = preorder[1:lenLeftSubtree+1]
    rightPreOrder = preorder[lenLeftSubtree+1:]

    leftChild = buildTree(leftPreOrder, leftInorder)
    rightChild = buildTree(rightPreOrder, rightInorder)

    rootNode.left = leftChild
    rootNode.right = rightChild
    return rootNode


preorder = [int(ele) for ele in input().split()]
inorder = [int(ele) for ele in input().split()]
root = buildTree(preorder, inorder)
bt = binaryTreeMethods()
bt.printLevelWise(root)
