# problem:- https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


def removeDuplicates(nums):
    ptr1 = 0
    ptr2 = 1
    n = len(nums)
    while(ptr2<n):
        if nums[ptr1] == nums[ptr2]:
            ptr2+=1
        else:
            ptr1+=1
            nums[ptr1] = nums[ptr2]
            ptr2+=1
    return ptr1+1


nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums)) # 5