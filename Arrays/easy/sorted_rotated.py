# Prroblem Link:- https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

def check(nums):
    n = len(nums)
    break_condition = 0
    for i in range(1,n):
        if nums[i]<nums[i-1]:
            break_condition+=1
    if break_condition>1:
        return False
    else:
        return True
    
nums = [3,4,5,1,2]
print(check(nums)) # True

