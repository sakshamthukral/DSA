# Link: https://leetcode.com/problems/move-zeroes/

def move_zeros(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    zero_index = -1
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_index = i
            break
    if zero_index == -1: # No zeros present
        return
    for i in range(zero_index+1, len(nums)):
        if nums[i]!=0:
            nums[i], nums[zero_index] = nums[zero_index], nums[i]
            zero_index+=1

nums = [0,1,0,3,12]
move_zeros(nums) 
print(nums) # [1, 3, 12, 0, 0]
