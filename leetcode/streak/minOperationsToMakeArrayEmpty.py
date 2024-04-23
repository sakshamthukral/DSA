from typing import List
from collections import Counter
import math
# Memorization + DP approach
def minOperations1(nums:List[int])->int:
    cache = {}
    def dfs(n):
        if n<0:
            return float("inf")
        if n in [2,3]:
            return 1
        if n in cache:
            return cache[n]
        ops = min(dfs(n-2),dfs(n-3))
        if ops == -1:
            return -1
        cache[n] = ops+1
        return ops+1

    freq = Counter(nums)
    res = 0
    for key, val in freq.items():
        operations = dfs(val)
        if operations == -1:
            return -1
        res+=operations
    return res
    
def minOperations2(nums:List[int])->int:
    freq = Counter(nums)
    operations = 0
    for key,val in freq.items():
        if val == 1:
            return -1
        operations+=math.ceil(val/3)
    return operations
nums = [int(ele) for ele in input().split()]
print(minOperations1(nums))
print(minOperations2(nums))
         
