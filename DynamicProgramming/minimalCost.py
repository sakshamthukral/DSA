# Memorization
def helper(heights, n, k, index, memo):
    if index >= n-1:
        return 0
    if memo[index] != -1:
        return memo[index]
    minCost = float('inf')
    for j in range(1,k+1):
        if index+j<n:
            cost = helper(heights, n, k, index+j, memo) + abs(heights[index] -  heights[index+j])
            minCost = min(minCost, cost)
    memo[index] = minCost
    return memo[index]

def minimalCost1(heights, n, k):
    index = 0
    memo = [-1]*n
    return helper(heights, n, k, index, memo)


# -----------------------------------------------------------------------------------------------------
# Tabulation
def minimalCost2(heights, n, k):
    dp = [-1]*n
    dp[0] = 0 # because min cost to reach the first index/step will definitely be 0
    for i in range(1,n):
        minCost = float('inf')
        for j in range(1,k+1):
            if i-j>=0:
                cost = dp[i-j] + abs(heights[i]-heights[i-j])
                minCost = min(minCost, cost)
        dp[i] = minCost
    return dp[n-1] # last index of the dp array will be storeing tha minimum cost to reach the last index

heights = [10, 30, 40, 50, 20]
n = 5
k=3
print(minimalCost1(heights, n, k)) # Memorization way (Top-down)
print(minimalCost2(heights, n, k)) # Tabulation way (Bottom-up)
