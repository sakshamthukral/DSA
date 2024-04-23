from BinaryTree import binaryTreeMethods, TreeNode
from typing import List
from collections import deque
# def printDequeu(q):
#     for ele in q:
#           print(ele.val,end=" ")
#     print()
def levelOrder(root:TreeNode)->List[List[int]]:
    if root == None:
        return []
    q = deque()
    q.append(root)
    result = []
    while(len(q)):
        level = []
        numElements = len(q)
        for i in range(numElements):
            currNode = q.popleft()
            level.append(currNode.val)
            if currNode.left:
                q.append(currNode.left)
            if currNode.right:
                q.append(currNode.right)
        result.append(level)
    return result

bt = binaryTreeMethods()
root = bt.inputLevelWise()
result = levelOrder(root)
print(result)
        


