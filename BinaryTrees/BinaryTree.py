import queue
class binaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None
class binaryTree:
    def __init__(self):
        self.root = None
    def printBinaryTreeHelper(self, root):
        if root == None:
            return
        print(root.data)
        self.printBinaryTreeHelper(root.left)
        self.printBinaryTreeHelper(root.right)
    def printBinaryTreeDetailedHelper(self, root):
        if root == None:
            return
        print(root.data,end=":")
        if root.left!=None:
            print(f"L {root.left.data}",end=",")
        if root.right!=None:
            print(f"R {root.right.data}",end=" ")
        print()
        self.printBinaryTreeDetailedHelper(root.left)
        self.printBinaryTreeDetailedHelper(root.right)
    def printBinaryTree(self):
        self.printBinaryTreeHelper(self.root)
    def printBinaryTreeDetailed(self):
        self.printBinaryTreeDetailedHelper(self.root)
    def takeTreeInputHelper(self):
        rootData=int(input())
        if rootData == -1:
            return None
        root = binaryTreeNode(rootData)
        leftTree=self.takeTreeInputHelper()
        rightTree=self.takeTreeInputHelper()
        if leftTree!=None:
            root.left=leftTree
        if rightTree!=None:
            root.right=rightTree
        return root
    def takeTreeInput(self):
        self.root = self.takeTreeInputHelper()
        return self.root
    def levelWiseTreeInputHelper(self):
        q = queue.Queue()
        print("Enter Root")
        rootData=int(input())
        if (rootData == -1):
         return None
        root = binaryTreeNode(rootData)
        q.put(root)
        while(not(q.empty())):
            current_node = q.get()
            print("Enter the left child of ",current_node.data)
            leftChildData = int(input())
            if leftChildData != -1:
                leftChild = binaryTreeNode(leftChildData)
                current_node.left = leftChild
                q.put(leftChild)
            print("Enter the right child of ", current_node.data)
            rightChildData = int(input())
            if rightChildData!=-1:
                rightChild = binaryTreeNode(rightChildData)
                current_node.right = rightChild
                q.put(rightChild)
        return root
    def levelWiseTreeInput(self):
        self.root = self.levelWiseTreeInputHelper()
        return self.root
    
    def levelWiseTreePrintHelper(self,root):
        q=queue.Queue()
        if root==None:
            return
        q.put(root)
        while(not(q.empty())):
            current_node = q.get()

            if current_node!=None:
                print(f"{current_node.data}:",end=" ")
            
            if current_node.left!=None:
                q.put(current_node.left)
                print(f"L {current_node.left.data}",end=", ")
            
            if current_node.right!=None:
                q.put(current_node.right)
                print(f"R {current_node.right.data}",end="")

            print()
        

    def levelWiseTreePrint(self):
        self.levelWiseTreePrintHelper(self.root)


# def printTreeDetailedExternal(root):
#     if root==None:
#         return 
#     print(root.data, end=":")
#     if root.left!=None:
#         print("L", root.left.data, end=",")
        
#     if root.right!=None:
#         print("R", root.right.data, end=" ")
#     print()
#     printTreeDetailed(root.left)
#     printTreeDetailed(root.right)
    
# bt=binaryTree()
# root = bt.takeTreeInput()
# printTreeDetailedExternal(root)