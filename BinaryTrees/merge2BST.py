from BinaryTree import binaryTreeNode
def buildTree(inorder):
     if len(inorder)==0:
         return
     mid = len(inorder)//2
     root = binaryTreeNode(inorder[mid])
     root.left = buildTree(inorder[:mid])
     root.right = buildTree(inorder[mid+1:])
     return root
def mergeSortedArrays(arr1, arr2):
    ptr1 = 0
    ptr2 = 0
    res=[]
    while(ptr1<len(arr1) and ptr2<len(arr2)):
        if arr1[ptr1]<=arr2[ptr2]:
            res.append(arr1[ptr1])
            ptr1+=1
        else:
            res.append(arr2[ptr2])
            ptr2+=1
    while(ptr1<len(arr1)):
        res.append(arr1[ptr1])
        ptr1+=1
    while(ptr2<len(arr2)):
        res.append(arr2[ptr2])
        ptr2+=1
    return res
            
        
def getInorder(root, inorder):
    if root==None:
        return
    getInorder(root.left, inorder)
    inorder.append(root.data)
    getInorder(root.right, inorder)
        
def merge(root1, root2):
    ino1, ino2=[],[]
    getInorder(root1, ino1)
    getInorder(root2, ino2)
    finalTree = mergeSortedArrays(ino1, ino2)
    finalRoot = buildTree(finalTree)
    bn = binaryTreeNode(finalRoot)
    bn.printBinaryTreeDetailed()

