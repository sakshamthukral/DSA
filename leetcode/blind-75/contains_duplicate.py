from typing import List
def containsDuplicate(nums: List[int]) -> bool:
        flag=False
        frequency_count={}
        for ele in nums:
            if ele in frequency_count:
                frequency_count[ele]+=1
            else:
                frequency_count[ele]=1
        for value in frequency_count.values():
            if value>1:
                flag = True
                return flag
        return flag
            
print("Input nums",end=": ")
nums = [int(ele) for ele in input().split()]
res = containsDuplicate(nums)
print(res)