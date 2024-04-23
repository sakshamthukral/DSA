# Logic :- We know that inorder traversal of a BST gives us all the elements in increasing sorted order. 
# So kth smallest element can be the kth element of inorder traversal of BST. Now we can traverse BST in 3 different ways, recursive way, 
# iterative way and morris traversal way. Solution with recursive and iterative way will give time complexity of O(n) but will also give space complexity of O(n).
# So we can use Morris Traversal to optimize space complexity to O(1)
from BinaryTree import binaryTreeMethods
def kthSmallest(root,k):
    counter = 0
    curr = root
    while(curr!=None):
        if curr.left == None:
            counter+=1
            if counter == k:
                return curr.val
            curr = curr.right
        else:
            prev = curr.left
            while(prev.right!=None and prev.right!=curr):
                prev = prev.right
            if prev.right == None:
                prev.right = curr # create thread
                curr = curr.left
            else: #prev.right==curr
                prev.right = None
                counter+=1
                if counter == k:
                    return curr.val
                curr = curr.right
    return -1

bt = binaryTreeMethods()
root = bt.inputLevelWise()
print("Input the value of k",end=": ")
k = int(input())
print(kthSmallest(root,k))
