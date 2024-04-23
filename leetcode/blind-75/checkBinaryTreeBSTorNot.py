from BinaryTree import binaryTreeMethods

def minMaxBinaryTree(root):
    if root == None:
        return float("inf"),float("-inf")
    if root.left == None and root.right == None:
        return root.val,root.val
    minLeft, maxLeft = minMaxBinaryTree(root.left)
    minRight, maxRight = minMaxBinaryTree(root.right)

    minTree = min(root.val, minLeft, minRight)
    maxTree = max(root.val, maxLeft, maxRight)
    return minTree,maxTree

def checkBST1(root): # Time complexity:- O(n^2)
    if root == None:
        return True
    if root.left == None and root.right == None:
        return True
    leftSubtreeMin, leftSubtreeMax = minMaxBinaryTree(root.left)
    rightSubtreeMin, rightSubtreeMax = minMaxBinaryTree(root.right)
    return leftSubtreeMax<root.val and rightSubtreeMin>root.val and checkBST1(root.left) and checkBST1(root.right)

def checkBST2(root):
    if root == None:
        return float("inf"),float("-inf"),True
    if root.left == None and root.right == None:
        return root.val,root.val,True
    minLeft, maxLeft, isLeftBST = checkBST2(root.left)
    minRight, maxRight, isRightBST = checkBST2(root.right)
    isTreeBST = True
    if not isLeftBST or not isRightBST or not root.val>maxLeft or not root.val<minRight:
        isTreeBST = False

    isTreeBST = isTreeBST and isLeftBST and isRightBST
    minTree = min(root.val, minLeft, minRight)
    maxTree = max(root.val, maxLeft, maxRight)
    return minTree,maxTree,isTreeBST

def checkBST3(root,minRange, maxRange):
    if root == None:
        return True
    if root.val<=minRange or root.val>=maxRange:
        return False
    isLeftWithinConstraints = checkBST3(root.left, minRange, root.val)
    isRightWithinConstraints = checkBST3(root.right, root.val, maxRange)
    return isLeftWithinConstraints and isRightWithinConstraints
    
bt = binaryTreeMethods()
root = bt.inputLevelWise()
# minT,maxT = minMaxBinaryTree(root)
res1 = checkBST1(root)
res2 = checkBST2(root)
res3 = checkBST3(root, float("-inf"),float("inf"))

print(res1)
print(res2)
print(res3)

    
    