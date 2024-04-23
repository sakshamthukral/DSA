from BinaryTree import binaryTree
def elementsInRangeK1K2(root, k1, k2):
    if root == None:
        return
    if root.data<k1:
        elementsInRangeK1K2(root.right,k1,k2)
    elif root.data>k2:
        elementsInRangeK1K2(root.left,k1,k2)
    else:
        elementsInRangeK1K2(root.left, k1, k2)
        print(root.data,end=" ")
        elementsInRangeK1K2(root.right,k1,k2)

bt=  binaryTree()
root = bt.levelWiseTreeInput()
print("Enter the value of k1: ")
k1 = int(input())
print("Enter the value of k2: ")
k2 = int(input())
elementsInRangeK1K2(root,k1,k2)
