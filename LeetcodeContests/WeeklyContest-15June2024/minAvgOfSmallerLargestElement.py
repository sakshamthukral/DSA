from typing import List
def minimumAverage(nums: List[int]) -> float:
        nums.sort()
        i=0
        j=len(nums)-1
        minElement = float('inf')
        while(i<j):
            avg = (nums[i]+nums[j])/2
            minElement = min(minElement, avg)
            i+=1
            j-=1
    
        return minElement

nums = [7,8,3,4,15,13,4,1]

print(minimumAverage(nums)) # 7.5