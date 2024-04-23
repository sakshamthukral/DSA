from typing import List

# Note: The two pointer approach won't work in this problem, as for using two pointer approach we will have to first sort the array and then make operations which will thereby loos the information of actual indices of the numbers in the array

def twoSum(nums:List[int], target:int)->List[int]:
    num_indices={}
    result = []
    for i, num in enumerate(nums):
        complement = target-num
        if complement in num_indices:
            result.append(num_indices[complement])
            result.append(i)
            break
        else:
            num_indices[num] = i
    return result

print("Input nums array: ")
nums = [int(ele) for ele in input().split()]
print("Input target Sum: ")
target = int(input())
result = twoSum(nums, target)
print(result)