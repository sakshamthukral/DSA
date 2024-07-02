from typing import List
def swap(nums, idx1, idx2):
    temp = nums[idx1]
    nums[idx1] = nums[idx2]
    nums[idx2] = temp

def helper(nums, index, ans):
    if index == len(nums):
        ans.append(nums[:])
        return
    for i in range(index, len(nums)):
        swap(nums, index, i)
        helper(nums, index+1, ans) # here instead of doing i+1, because here we need to find the permutations of the array, starting from each index of the array ans we don't want to skip any element as we do while finding the subsets
        swap(nums, i, index)

def permute(nums: List[int]) -> List[List[int]]:
    index = 0
    ans = []
    helper(nums, index, ans)
    return ans

nums = [1,2,3]
print(permute(nums))