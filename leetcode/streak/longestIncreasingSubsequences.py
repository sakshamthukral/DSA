from typing import List
def f(index:int, prev_index:int, nums:List[int], n, dp):
    if index == n:
        return 0
    if dp[index][prev_index+1] != -1:
        return dp[index][prev_index+1]
    l = 0 + f(index+1, prev_index, nums, n, dp) # Don't take case, i.e. not considering the current element as part of subsequence
    if prev_index == -1 or nums[index]>nums[prev_index]:
        l = max(l, 1 + f(index+1, index, nums, n, dp)) # take case, i.e. considering the current element as part of subsequence
    dp[index][prev_index+1] = l
    return l

def LIS1(nums:List[int])->int: # Time complexity:- O(n^2), Space Complexity:- O(n)
    n = len(nums)
    rows = n+1
    columns = n
    dp = [[-1]*columns for _ in range(rows)]

    return f(0,-1,nums,n,dp)

#----------------------------------------------------------------------------------------------------------
# Tabular Approach : Time complexity:- O(n^2) , Space Complexity:- O(n), for dp array
def LIS2(nums:List[int])->int:
    n = len(nums)
    dp = [1]*n
    for i in range(n):
        for prev in range(i):
            if nums[prev]<nums[i]:
                dp[i] = max(dp[i], 1+dp[prev])
    
    maxi = max(dp)
    return maxi

#------------------------------------------------------------------------------------------------------------
# Print longest increasing subsequence
def printLIS(nums:List[int]):
    n = len(nums)
    dp = [1]*n
    maxi = 1
    last_index = 0
    backtrack = list(range(n))
    for i in range(n):
        for prev in range(i):
            if nums[prev]<nums[i] and dp[i] < 1+dp[prev]:
                dp[i] = 1+dp[prev]
                backtrack[i] = prev
        
        if dp[i]>maxi:
            maxi = dp[i]
            last_index = i
    
    temp = []
    temp.append(nums[last_index])
    while(backtrack[last_index]!=last_index):
        last_index = backtrack[last_index]
        temp.append(nums[last_index])
    temp = temp[::-1]
    print(temp)
    return maxi
#-------------------------------------------------------------------------------------------------



def lowerBound(nums:List[int],ele):
    if len(nums) == 1:
        return 0
    si = 0
    ei = len(nums)
    mid = -1
    while(si<=ei):
        mid = (si+ei)//2
        if nums[mid] == ele:
            return mid
        elif ele<nums[mid]:
            ei = mid-1
        else:
            si = mid+1
    if nums[mid] != ele:
        if nums[mid]<ele:
            return mid+1
        else:
            return mid

def LIS3(nums:List[int])->int:
    sequence = []
    sequence.append(nums[0])
    len_sequence = 1
    for i in range(1, len(nums)):
        if nums[i]>sequence[-1]:
            sequence.append(nums[i])
            len_sequence+=1
        else:
            indexToReplace = lowerBound(sequence,nums[i])
            sequence[indexToReplace] = nums[i]
    return len_sequence



nums = [int(ele) for ele in input().split()]
print(LIS1(nums))
print(LIS2(nums))
print(LIS3(nums))
print(printLIS(nums))
# print(lowerBound(nums,23))