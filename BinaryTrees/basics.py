from BinaryTree import binaryTree


def countNodes(root):
    if root == None:
        return 0
    leftCount = countNodes(root.left)
    rightCount = countNodes(root.right)
    return 1+leftCount+rightCount

def largestNode(root):
    if root==None:
        return -100000
    leftLargestData = largestNode(root.left)
    rightLargestData = largestNode(root.right)
    return max(root.data, leftLargestData, rightLargestData)

def heightOfTree(root):
    if root==None:
        return 0
    leftHeight = heightOfTree(root.left)
    rightHeight = heightOfTree(root.right)
    return 1 + max(leftHeight,rightHeight)

def sumOfNodes(root):
    if root==None:
        return 0
    sumLeft = sumOfNodes(root.left)
    sumRight = sumOfNodes(root.right)
    return root.data+sumLeft+sumRight
def preOrderTraversal(root):
    if root==None:
        return 
    print(root.data,end=" ")
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

def postOrderTraversal(root):
    if root==None:
        return 
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.data, end=" ")

def nodesGreaterThanX(root,x):
    if root==None:
        return 0
    leftCount = nodesGreaterThanX(root.left,x)
    rightCount = nodesGreaterThanX(root.right,x)
    if root.data>x:
        return 1+leftCount+rightCount
    else:
        return leftCount+rightCount
     
def nodesAtDeptk(root,k):
    if root==None:
        return
    if k==0:
        print(root.data)
        return
    nodesAtDeptk(root.left,k-1)
    nodesAtDeptk(root.right,k-1)
    
def nodesWithDepth(root,d=0):
    if root==None:
        return None
    root.data = d
    nodesWithDepth(root.left,d+1)
    nodesWithDepth(root.right,d+1)
    return root

def findNode(root,node):
    if root == None:
        return False
    if root.data == node:
        return True
    searchLeft = findNode(root.left,node)
    searchRight = findNode(root.right,node)
    return searchLeft or searchRight

def printNodesWithoutSibblings(root):
    if root == None:
        return
    if root.left==None and root.right!=None:
        print(root.right.data)
    elif root.left!=None and root.right==None:
        print(root.left.data)
    printNodesWithoutSibblings(root.left)
    printNodesWithoutSibblings(root.right)


bt=binaryTree()
# x=int(input())
# k=int(input())
# node=int(input())
root = bt.takeTreeInput()
# print(countNodes(root))
# print(largestNode(root))
# print(heightOfTree(root))
# print(sumOfNodes(root))
# print()
# preOrderTraversal(root)
# print()
# postOrderTraversal(root)
# print()
# print(nodesGreaterThanX(root,x))
# nodesAtDeptk(root,k)
bt.printBinaryTreeDetailed()
# updated_root = nodesWithDepth(root)
# bt.printBinaryTreeDetailedHelper(updated_root)
# print(findNode(root,node))
printNodesWithoutSibblings(root)