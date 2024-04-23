from typing import List

def maxSubarraySum(nums: List[int])-> List[int]:
    maxSum = float('-inf')
    currentSum = 0
    for num in nums:
        currentSum+=num
        if currentSum > maxSum:
            maxSum = currentSum
        if currentSum<0:
            currentSum = 0
    return maxSum

print("Input nums",end=": ")
nums = [int(ele) for ele in input().split()]
res = maxSubarraySum(nums)
print(res)

# Notes:- There's an assumption that we consider for this program i.e. maxSum can't be negative, it's value will always be greater than 0