# problem:- https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Approach:- 2 pointer approach. We will keep 2 pointers ptr1 and ptr2. ptr1 will be at 0th index and ptr2 will be at 1st index. We will compare the elements at ptr1 and ptr2. If they are same, we will increment ptr2. If they are different, we will increment ptr1 and copy the element at ptr2 to ptr1 and increment ptr2. We will keep on doing this until ptr2 reaches the end of the array. The length of the array will be ptr1+1.
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