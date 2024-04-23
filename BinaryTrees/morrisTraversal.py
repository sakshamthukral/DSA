from BinaryTree import binaryTree

def morrisTraversalInorder(root):
    inorder = []
    cur = root
    while cur!=None:
        if cur.left == None:
            inorder.append(cur.data)
            cur = cur.right
        else:
            prev = cur.left
            while(prev.right!=None and prev.right!=cur):
                prev = prev.right
            if prev.right == None:
                prev.right = cur # creating thread
                cur = cur.left
            else: # prev.right == cur
                prev.right = None # removing thread if thread already exists
                inorder.append(cur.data)
                cur = cur.right
    return inorder

# Question:- Why we create thread?
# Answer:- We create thread as a symbol depicting that left tree has been already traversed and now it right tree's turn. 
# If thread doesn't exist in right most node of tree, that means left tree has not yet been traversed and we move to left subtree.
# If thread exists that depicts left tree has been fully traversed and it's our turn now to traverse the right subtree, and we remove 
# the thread during right subtree traversal to maintain the original structure of the Binary Tree.


bt = binaryTree()
root = bt.levelWiseTreeInput()
inorder = morrisTraversalInorder(root)
print(inorder)