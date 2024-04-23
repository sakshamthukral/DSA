from BinaryTree import binaryTreeMethods

def maxPathSum(root):
    def dfs(root):
        nonlocal maxSum
        if root == None:
            return 0
        
        # Getting the max sum from the left and the right subtrees
        maxLeftSum = max(0, dfs(root.left))
        maxRightSum = max(0, dfs(root.right))

        # Then comparing the value of maxSum and the sum computed by adding values from left subtree, right subtree and the current node. 
        # This step considers the case which decides whehter node's value helps in increasing the value of maxSum or not and change the value of maxSum accordingly
        maxSum = max(maxSum, maxLeftSum+maxRightSum+root.val)

        # Return the maximum path sum of the subtree rooted at the current node
        return max(maxLeftSum, maxRightSum)+root.val
    maxSum = float("-inf")
    dfs(root)
    return maxSum


bt = binaryTreeMethods()
root = bt.inputLevelWise()
print(maxPathSum(root))