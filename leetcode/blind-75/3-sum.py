from typing import List

def threeSum(nums:List[int])->List[List[int]]:
    nums.sort()
    triplets = set()
    n=len(nums)
    for i in range(len(nums)-2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        firstNum = nums[i]
        j=i+1
        k=n-1
        while(j<k):
            secondNum, thirdNum = nums[j],nums[k]
            tripletSum = firstNum+secondNum+thirdNum
            if tripletSum<0:
                j+=1
            elif tripletSum>0:
                k-=1
            else:
                triplets.add((firstNum,secondNum,thirdNum))
                j,k=j+1,k-1
            
            while(j<k and nums[j]==nums[j+1]): # till the time we have same element, keep moving forward
                j+=1
            while(j<k and nums[k]==nums[k-1]): # till the time we have same element, keep moving backward
                k-=1
        
    return triplets

print("Input nums",end=": ")
nums = [int(ele) for ele in input().split()]
triplets = threeSum(nums)
print(triplets)
