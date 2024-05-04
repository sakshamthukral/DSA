from typing import List


def maxSubArray(nums:List[int])->int:
    sum_res = 0 
    maxi = float('-inf')

    for i in range(len(nums)):
        sum_res+=nums[i]
        if sum_res>maxi:
            maxi = sum_res
        if sum_res<0:
            sum_res=0
        # if maxi<0:
        #     maxi=0
    return maxi

def maxSubArray_kadanesExtended(nums:List[int])->List[int]:
    sum_res = 0
    maxi = float('-inf')
    start_idx = -1
    end_idx = -1
    start = -1
    for i in range(len(nums)):
        if sum_res == 0:
            start = i
        sum_res += nums[i]
        if sum_res>maxi:
            maxi = sum_res
            start_idx = start
            end_idx = i

        if sum_res<0:
            sum_res=0
    return (maxi, start_idx, end_idx)



# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-2,-11,-3,-4,-5]
# print(maxSubArray(nums))
print(maxSubArray_kadanesExtended(nums))




