from typing import List
def numberGame(nums: List[int]) -> List[int]:
    nums.sort()
    n=len(nums)
    arr = []
    for i in range(0,n-1,2):
        alice_pick = nums[i]
        bob_pick = nums[i+1]
        arr.append(bob_pick)
        arr.append(alice_pick)
    return arr


nums = [int(ele) for ele in input().split()]
result = numberGame(nums)
print(result)