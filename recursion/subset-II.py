from typing import List
def helper(nums, index, subset, ans):
    ans.append(subset[:])
    if index>=len(nums):
        return
    for i in range(index, len(nums)):
        if i > index and nums[i] == nums[i-1]:
            continue
        subset.append(nums[i])
        helper(nums, i+1, subset, ans)
        subset.pop()


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    index = 0
    ans = []
    subset = []
    helper(nums, index, subset, ans)
    return ans

nums = [1,2,2]
print(subsetsWithDup(nums))