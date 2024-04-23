from BinaryTree import binaryTree
from BinaryTree import binaryTreeNode
import queue

def removeLeafNodes(root):
    if root==None:
        return None
    if root.left==None and root.right==None:
        return None
    leftRoot = removeLeafNodes(root.left)
    rightRoot = removeLeafNodes(root.right)
    root.left=leftRoot
    root.right=rightRoot
    return root

def getHeightAndCheckBalance(root, height):
    pass

# def checkBalanced(root):
#     if root==None:
#         return True, 0
#     lh, isLeftBalanced = checkBalanced(root.left)
#     rh, isRightBalanced = checkBalanced(root.right)
#     h=1+max(lh,rh) # calculating height in every recursive call
#     if lh-rh>1 or rh-lh>1:
#         return h, False # checking for height condition based on which we will be returning value as True or False
#     if isLeftBalanced and isRightBalanced:
#         return h, True
#     else:
#         return h, False
    
def checkBalanced(root):
    if root is None:
        return True, 0
    
    isLeftBalanced, lh = checkBalanced(root.left)
    isRightBalanced, rh = checkBalanced(root.right)
    
    h = 1 + max(lh, rh)  # calculate height only when the tree is balanced

    if lh - rh > 1 or rh - lh > 1:
        return False, h  # checking for height condition based on which we will be returning value as True or False
    
    if isLeftBalanced and isRightBalanced:
        return True, h
    else:
        return False, h

def height(root):
    if root==None:
        return 0
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    return 1 + max(leftHeight,rightHeight)


def getDiameter1(root):
    if root == None:
        return 0
    lHeight = height(root.left)
    rHeight = height(root.right)

    lDiameter = getDiameter1(root.left)
    rDiameter = getDiameter1(root.right)
    
    return max(1+lHeight+rHeight,max(lDiameter,rDiameter))
    
def getDiameterHelper2(root):
    if root==None:
        return 0,0
    lh, ld = getDiameterHelper2(root.left)
    rh, rd = getDiameterHelper2(root.right)
    
    treeHeight = max(lh,rh)+1
    return treeHeight,max(1+lh+rh,max(ld,rd))
def getDiameter2(root):
    height, diameter = getDiameterHelper2(root)
    return diameter

def treeUsingPreorderAndInorder(preorder,inorder):
    if len(preorder)==0:
        return
    rootData = preorder[0]
    root = binaryTreeNode(rootData)
    rootIndexInorder = -1
    for i in range(len(inorder)):
        if inorder[i] == rootData:
            rootIndexInorder=i
            break
    if rootIndexInorder == -1:
        return None
    leftInorder = inorder[0:rootIndexInorder]
    rightInorder = inorder[rootIndexInorder+1:]
    lenLeftSubtree = len(leftInorder)
    
    leftPreOrder = preorder[1:lenLeftSubtree+1]
    rightPreOrder = preorder[lenLeftSubtree+1:]

    leftChild = treeUsingPreorderAndInorder(leftPreOrder,leftInorder)
    rightChild = treeUsingPreorderAndInorder(rightPreOrder,rightInorder)

    root.left = leftChild
    root.right = rightChild
    return root

def treeUsingInorderAndPostorder(inorder,postorder):
    if len(postorder) == 0:
        return
    rootData = postorder[-1]
    root = binaryTreeNode(rootData)
    rootIndexInorder = -1
    for i in range(len(inorder)):
        if inorder[i] == rootData:
            rootIndexInorder = i
    leftInorder = inorder[0:rootIndexInorder]
    rightInorder = inorder[rootIndexInorder+1:]

    lenLeftInorder = len(leftInorder)

    leftPostorder = postorder[0:lenLeftInorder]
    rightPostOrder = postorder[lenLeftInorder:-1]

    leftChild = treeUsingInorderAndPostorder(leftInorder,leftPostorder)
    rightChild = treeUsingInorderAndPostorder(rightInorder,rightPostOrder)
    
    root.left = leftChild
    root.right = rightChild
    return root

def createAndInsertDuplicate(root):
    if root == None:
        return
    createAndInsertDuplicate(root.left)
    createAndInsertDuplicate(root.right)

    if root.left == None:
        duplicate = binaryTreeNode(root.data)
        root.left = duplicate
    else:
        left_node = root.left
        duplicate = binaryTreeNode(root.data)
        duplicate.left = left_node
        root.left = duplicate
    return root

class Pair :
    def __init__(self, minimum, maximum) :
        self.minimum = minimum
        self.maximum = maximum

def getMinAndMaxHelper(root, minimum, maximum):
    if root == None:
        return 100000,-100000
    min_left, max_left = getMinAndMaxHelper(root.left, minimum, maximum)
    min_right, max_right = getMinAndMaxHelper(root.right, minimum, maximum)

    return min(min_left,min_right, root.data), max(max_left,max_right, root.data)

def getMinAndMax(root):
    minimum, maximum = getMinAndMaxHelper(root,100000,-100000)
    pair = Pair(minimum, maximum)
    return pair

def levelwisePrintTree(root):
    if root == None:
        return
    q = queue.Queue()
    q.put(root)
    q.put(None)
    while(not(q.empty())):
        element = q.get()
        if element == None:
            if not q.empty():
                q.put(None)
                print()
        else:
            print(element.data,end=" ")
            if element.left!=None:
                q.put(element.left)
            if element.right!=None:
                q.put(element.right)
    # print()

def mirrotTree(root):
    if (root==None) or (root.left==None and root.right==None):
        return
    mirrotTree(root.left)
    mirrotTree(root.right)

    if root.left==None and root.right!=None:
        root.left = root.right
        root.right = None
    elif root.left!=None and root.right==None:
        root.right = root.left
        root.left=None
    else:
        leftTree = root.left
        root.left = root.right
        root.right = leftTree
    return root

def rootToLeafPathSumToKHelper(root, k, path, allPaths):
    if root == None:
        return
    
    path.append(root.data)
    if root.left == None and root.right == None and k-root.data == 0:
        allPaths.append(path.copy())
        path.pop()
        return
    
    rootToLeafPathSumToKHelper(root.left, k-root.data, path, allPaths)
    rootToLeafPathSumToKHelper(root.right, k-root.data, path, allPaths)
    path.pop()

def rootToLeafPathSumToK(root, k):
    allPaths = []
    rootToLeafPathSumToKHelper(root,k,[],allPaths)
    return allPaths

def printkDistanceNodesDown(root,k):
    if root == None or k<0:
        return 
    if k==0:
        print(root.data)
        return
    printkDistanceNodesDown(root.left, k-1)
    printkDistanceNodesDown(root.right, k-1)
    
def printkDistanceNode(root,target,k):
    # base case
    if root == None:
        return -1
    if root.data == target:
        printkDistanceNodesDown(root,k)
        return 0
    dl = printkDistanceNode(root.left, target, k) # it can have either -1 or 0 as values. -1 from base case(if target node not found), and 0 otherwise (if target node found).
    if dl!=-1: # target node found on left side
        if dl+1 == k:
            print(root.data)
        else:
            printkDistanceNodesDown(root.right, k-dl-2)
        return 1+dl
    
    # check if the target node found in the right subtree
    dr = printkDistanceNode(root.right, target, k)
    if dr!=-1: # target node found in the right subtree
        if dr+1==k:
            print(root.data)
        else:
            printkDistanceNodesDown(root.left, k-dr-2)
        return 1+dr
    
    # if target node was neither found in left subtree and nor in right subtree, return -1
    return -1



# def levelwisePrintTree(root):
#     if root is None:
#         return

#     q = queue.Queue()
#     q.put(root)
#     q.put(None)  # Using None as a marker for the end of each level

#     while not q.empty():
#         element = q.get()

#         if element is None:
#             if not q.empty():
#                 q.put(None)  # Add marker for the next level
#                 print()  # Move to the next line
#         else:
#             print(element.data, end=" ")

#             if element.left is not None:
#                 q.put(element.left)

#             if element.right is not None:
#                 q.put(element.right)




bt = binaryTree()
# root = bt.takeTreeInput()
root = bt.levelWiseTreeInput()
# preorder = [10,11,13,14,15,7]
# inorder = [14,13,15,11,10,7]
# postorder = [14,15,13,11,7,10]
# root = treeUsingPreorderAndInorder(preorder,inorder)
# bt.levelWiseTreePrintHelper(root)
# print("___________________________________________________")
# root = treeUsingInorderAndPostorder(inorder,postorder)
# bt.levelWiseTreePrintHelper(root)
# new_root = removeLeafNodes(root)

# bt.printBinaryTreeDetailedHelper(new_root)
# balanced, h = checkBalanced(root)
# print(balanced)

# treeDiamater1 = getDiameter1(root)
# treeDiamater2 = getDiameter2(root)
# print(f"Diamater 1 : {treeDiamater1}")
# print(f"Diamater 2 : {treeDiamater2}")

# duplicatedTree = createAndInsertDuplicate(root)
# bt.levelWiseTreePrintHelper(duplicatedTree)
# pair_result = getMinAndMax(root)
# print(pair_result.minimum)
# print(pair_result.maximum)
# mirrorRoot = mirrotTree(root)
levelwisePrintTree(root)
print("________________________________________")
# print("Enter the target value",end=" : ")
# target=int(input())
# print("Enter the value of k",end=" : ")
# k=int(input())
# paths = rootToLeafPathSumToK(root, k)
# print(paths)
# bt.levelWiseTreePrintHelper(mirrorRoot)
printkDistanceNode(root, 8, 2)
