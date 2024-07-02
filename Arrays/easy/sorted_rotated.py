# Prroblem Link:- https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/


# Approach:- Compare all the elements of the array with the previous element. If the current element is less than the previous element, increment the break_condition. If the break_condition is greater than 1 or less than 1, return False. Otherwise, return True.
# We need to compare all the selements in a cycle fashion. So, we need to compare the last element with the first element as well.
# if the break_condition is 1 or less than 1, then it's fine , but if the break condition is greater than 1, it will signify that condition has been violated more than once and the array is not sorted or can't be rotated to make it sorted.
def check(nums):
    n = len(nums)
    break_condition = 0
    for i in range(1,n):
        if nums[i]<nums[i-1]:
            break_condition+=1
    
    if nums[n-1]>nums[0]: # If a rotation is expected to happend then the last element should be less than the first element otherwise it will also be considered as a break condition.
        break_condition+=1
    return break_condition <= 1 # instead of check break_condition == 1, we are checking break_condition <= 1 because if the all the elements of the array are duplicates then break_condition will be 0 in that case which also means that the array is sorted or can be rotated to make it sorted.
    
nums = [3,4,5,1,2]
print(check(nums)) # True

