
def recursiveSubsets(nums, index, n , subset, finalAns):
    if index >= n:
        finalAns.append(subset[:]) # to store the copy of the subset, doing this finalAns.append(subset[:]) will store a reference which will give wrong output
        return 
    subset.append(nums[index])
    recursiveSubsets(nums, index+1, n, subset, finalAns) # Take Case
    subset.pop()
    recursiveSubsets(nums, index+1, n, subset, finalAns) # Not Take Case


def subsets(nums):
    finalAns = []
    recursiveSubsets(nums, 0, len(nums), [], finalAns)
    return finalAns


nums = [1,2,3]
print(subsets(nums))