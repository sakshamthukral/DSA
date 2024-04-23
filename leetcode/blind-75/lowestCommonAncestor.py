from BinaryTree import binaryTreeMethods,TreeNode

def lca(root, n1, n2):
 
    # Base Case
    if root is None:
        return None
 
    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(root.val > n1 and root.val > n2):
        return lca(root.left, n1, n2)
 
    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if(root.val < n1 and root.val < n2):
        return lca(root.right, n1, n2)
 
    return root

bt = binaryTreeMethods()
root = bt.inputLevelWise()
print("Enter p",end=": ")
p = int(input())
print("Enter q",end=": ")
q = int(input())
res = lca(root,TreeNode(p),TreeNode(q))
print(res.val)