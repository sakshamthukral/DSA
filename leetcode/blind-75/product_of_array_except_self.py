from typing import List

def productExceptSelf(nums: List[int])->List[int]:
    prefix_product = 1
    result = [1]*len(nums)
    for i, num in enumerate(nums):
        result[i] *= prefix_product
        prefix_product *= num
    postfix_product = 1
    for i in range(len(nums)-1,-1,-1):
        result[i] *= postfix_product
        postfix_product *= nums[i]
    return result

print("Input nums",end=": ")
nums = [int(ele) for ele in input().split()]
res = productExceptSelf(nums)
print(res)  

# Notes: Using concept of generating prefix and postfix arrays. Since array creation will consume space and 
# will give O(n) space complexity, so we can achieve the same thing withou explicitly creating arrays ultimately optimizing 
# space complexity to O(1).
# So, time complexity :- O(n), and Space Complexity :- O(1)