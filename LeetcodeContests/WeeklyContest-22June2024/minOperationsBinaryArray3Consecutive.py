# Problem Link: https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/
from typing import List
# Recursive Approach: Time Complexity: O(2^n), Space Complexity: O(n)
# def all1s(nums):
#     for i in nums:
#         if i == 0:
#             return False
#     return True
# def flip(nums, index):
#     for i in range(index, index+3):
#         if nums[i] == 0:
#             nums[i] = 1
#         else:
#             nums[i] = 0
#     return nums
# def helper(nums, index, operations, count):
#     if all1s(nums):
#         count[0] = min(count[0], operations)
#         return
#     if index > len(nums)-3:
#         return
    
#     flip(nums, index)
#     helper(nums, index+1, operations+1, count) # flip the current index
#     flip(nums, index) # undo the flip
#     helper(nums, index+1, operations, count) # don't flip the current index

# def minOperationsBinaryArray(nums:List[int]) -> int:
#     count = [float('inf')]
#     index = 0
#     helper(nums, index, 0, count)
#     return count[0] if count[0]!=float('inf') else -1

# arr = [0,1,1,1,0,0]
# print(minOperationsBinaryArray(arr)) # sample output: 2
#-----------------------------------------------------------------------------------------------------
# Iterative Approach: Time Complexity: O(n), Space Complexity: O(1)

def minOperationsBinaryArray(nums: List[int]) -> int:
    n = len(nums)
    operations = 0
    
    for i in range(n - 2):  # Go only up to n-3, since we're flipping triplets
        if nums[i] == 0:
            # Perform a flip operation on the triplet starting at index i
            for j in range(i, i + 3):
                nums[j] = 1 if nums[j] == 0 else 0
            operations += 1

    # Check if there are any 0s left in the last two elements
    if nums[-2] == 0 or nums[-1] == 0:
        return -1

    return operations

# Example
arr = [0, 1, 1, 1, 0, 0]
print(minOperationsBinaryArray(arr))  # Expected output: 3
