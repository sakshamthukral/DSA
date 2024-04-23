from BinaryTree import binaryTreeMethods,TreeNode
from collections import deque
def serialize(root):
    if root == None:
        return "#"
    q = deque()
    q.append(root)
    serializedTree = ""
    while q:
        node = q.popleft()
        if node:
            serializedTree+=str(node.val)+","
            q.append(node.left)
            q.append(node.right)
        else:
            serializedTree+="#,"
    return serializedTree

def deserialize(s):
    nodesData = s[:-1].split(',')
    rootData = nodesData[0]
    if rootData!="#":
        rootNode = TreeNode(rootData)
    else:
        return None
    TreeNodes = deque()
    TreeNodes.append(rootNode)
    i=1
    while TreeNodes and i<len(nodesData):
        root = TreeNodes.popleft()

        leftData = nodesData[i]
        i+=1
        if leftData!='#':
            leftNode = TreeNode(leftData)
            root.left = leftNode
            TreeNodes.append(leftNode)
        else:
            root.left = None
        rightData = nodesData[i]
        i+=1
        if rightData!='#':
            rightNode = TreeNode(rightData)
            root.right = rightNode
            TreeNodes.append(rightNode)
        else:
            root.right = None    

    return rootNode

bt = binaryTreeMethods()
root = bt.inputLevelWise()
bt.printLevelWise(root)
serializedTree = serialize(root)
print(serializedTree)
# deserialize(serializedTree)
deserializedRoot=deserialize(serializedTree)
bt.printLevelWise(deserializedRoot)