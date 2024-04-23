from typing import List

# Brute Force Approach-1 : Time Complexity- O(n^3) , Space Compexity- O(1)
def maxSubarrayProduct1(nums:List[int])->int:
    maxProduct = float('-inf')
    for i in range(0, len(nums)):
        for j in range(i,len(nums)):
            product=1
            for k in range(i,j+1):
                product*=nums[k]
            maxProduct = max(maxProduct,product)     

    return maxProduct

# Brute Force Approach-2 : Time Complexity- O(n^2) , Space Compexity- O(1)
def maxSubarrayProduct2(nums:List[int])->int: 
    maxProduct = float('-inf')
    for i in range(0, len(nums)):
        product=1
        for j in range(i,len(nums)):
            product*=nums[j]
            maxProduct = max(maxProduct,product)     

    return maxProduct
# Notes Appriach-2:- Instead of computing product each time as we were doing in approach-1, we can just multiply the last number(the new number added to subarray).


# Optimized Approach:- Time Complexity- O(n), Space Complexity- O(1)
def maxSubarrayProduct3(nums:List[int])->int: 
    maxProduct = float('-inf')
    for i in range(0, len(nums)):
        product=1
        for j in range(i,len(nums)):
            product*=nums[j]
            maxProduct = max(maxProduct,product)     

    return maxProduct

def maxSubarrayProduct3(nums:List[int])-> int:
    prefix = 1
    suffix = 1
    maxProduct = 1
    n = len(nums)
    for i in range(0, n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
        prefix *= nums[i]
        suffix *= nums[n-i-1]
        maxProduct = max(maxProduct,prefix,suffix)
    return maxProduct
# Notes for approach-3:- For approach-3 we made an observation that, for any number which we want to exclude in order to get the max prodcut, the answer will 
# either be in the prefix of the number, or the suffix of that number. So if we find the prefix and suffix product for each number, 
# and find their max, it will be our final maxProduct as well. In case we get 0 on computing prefix or suffix we will reset their values to 1
# and will again continue to compute prefix and suffix products for rest of the numbers, and comparing their max.
        


print("Input nums",end=": ")
nums = [int(ele) for ele in input().split()]
res1 = maxSubarrayProduct1(nums)
res2 = maxSubarrayProduct2(nums)
res3 = maxSubarrayProduct3(nums)
print(res1)
print(res2)
print(res3)