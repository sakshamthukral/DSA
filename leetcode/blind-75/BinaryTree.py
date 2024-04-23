import queue
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class binaryTreeMethods:
    def __init__(self):
        self.root = None
    def inputLevelWise(self):
        q = queue.Queue()
        print("Enter root")
        rootData = int(input())
        if rootData == -1:
            return None
        root = TreeNode(rootData)
        q.put(root)
        while(not(q.empty())):
            currentNode = q.get()
            print("Enter the left child of ", currentNode.val)
            leftData = int(input())
            if leftData!=-1:
                leftChild = TreeNode(leftData)
                currentNode.left = leftChild
                q.put(leftChild)
            print("Enter the right child of ", currentNode.val)
            rightData = int(input())
            if rightData!=-1:
                rightChild = TreeNode(rightData)
                currentNode.right = rightChild
                q.put(rightChild)
        self.root = root
        return root
    def printLevelWise(self,root):
        if root == None:
            print("None Root")
            return
        q = queue.Queue()
        q.put(root)
        while(not(q.empty())):
            currData = q.get()
            print(currData.val,end=" :")
            if currData.left!=None:
                leftChild = currData.left
                print(f"L{leftChild.val}",end=", ")
                q.put(leftChild)
            if currData.right!=None:
                rightChild = currData.right
                print(f"R{rightChild.val}",end="")
                q.put(rightChild)
            print()


        
