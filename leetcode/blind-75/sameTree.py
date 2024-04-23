from BinaryTree import binaryTreeMethods

def isSameTree(p,q):
    if p == None and q == None:
        return True
    elif p == None and q !=None:
        return False
    elif p !=None and q == None:
        return False
    if p.val!=q.val:
        return False
    return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)


bt = binaryTreeMethods()
p = bt.inputLevelWise()
q = bt.inputLevelWise()
print(isSameTree(p,q))