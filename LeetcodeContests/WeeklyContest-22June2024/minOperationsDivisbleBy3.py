# Problem Link:- https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/
from typing import List
def minimumOperations(nums: List[int]) -> int:
        operations = 0
        for i in range(len(nums)):
            if nums[i] % 3 == 0:
                continue
            elif (nums[i]+1) % 3 == 0:
                operations+=1
            elif (nums[i]-1) % 3 == 0:
                operations +=1
        return operations
arr = [3,6,9]
print(minimumOperations(arr)) # sample output: 3