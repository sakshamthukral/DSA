# Problem Link: https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/description/
from typing import List
def minOperationsBinaryArray(nums: List[int]) -> int:
    n = len(nums)
    operations = 0
    flipped = False
    
    for i in range(n):
        current_value = nums[i] if not flipped else 1 - nums[i]

        if current_value == 0:
            flipped = not flipped
            operations += 1
    return operations
# Example
arr = [0, 1,1, 0, 1]
print(minOperationsBinaryArray(arr))  # Expected output: 3