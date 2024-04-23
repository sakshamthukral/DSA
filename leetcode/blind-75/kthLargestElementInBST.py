from BinaryTree import binaryTreeMethods
# Question:- Need to find the kth Largest element in the BST in O(1) space

def countNodesMorrisTraversal(root):
    counter = 0
    curr = root
    while(curr!=None):
        if curr.left==None:
            counter+=1
            curr = curr.right
        else:
            prev = curr.left
            while(prev.right!=None and prev.right!=curr):
                prev = prev.right
            if prev.right == None:
                prev.right = curr
                curr = curr.left
            else: # prev.right == curr
                prev.right = None
                counter+=1
                curr = curr.right
    return counter


def kthLargestElement(root,k):
    numNodes = countNodesMorrisTraversal(root)
    smallestElementIndex = numNodes-k+1 # kth largest element meand (n-k+1)th smallest element, where n is the total number of nodes in the tree
    counter = 0
    curr = root
    while(curr!=None):
        if curr.left == None:
            counter+=1
            if counter == smallestElementIndex:
                return curr.val
            curr = curr.right
        else:
            prev = curr.left
            while(prev.right!=None and prev.right!=curr):
                prev = prev.right
            if prev.right == None:
                prev.right = curr
                curr = curr.left
            else: #prev.right == curr
                prev.right = None
                counter+=1
                if counter == smallestElementIndex:
                    return curr.val
                curr = curr.right
    return -1

# We are traversing the tree 2 times , once for counting the number of nodes, and second time to find the kth largest element.
# So time complexity will still be n+n or O(n) and and morris traversal takes O(1) space to space complexity will be O(1)


bt = binaryTreeMethods()
root = bt.inputLevelWise()
print("Enter the value of k",end=": ")
k=int(input())
print(kthLargestElement(root,k))