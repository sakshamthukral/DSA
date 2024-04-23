from typing import List

def findMatrix(nums:List[int])->List[List[int]]:
    result = []
    freq = {}
    # max_freq = float("-inf")
    for ele in nums:
        if ele in freq.keys():
            freq[ele]+=1
        else:
            freq[ele] = 1
        
        if freq[ele]-1<len(result):
            result[freq[ele]-1].append(ele)
        else:
            result.append([ele])
    #     max_freq = freq[ele] if freq[ele]>max_freq else max_freq

    # result = []
    # for i in range(max_freq):
    #     row = []
    #     for key in freq.keys():
    #         if freq[key]<=0:
    #             continue
    #         row.append(key)
    #         freq[key]-=1
    #     result.append(row)
    return result

nums = [int(ele) for ele in input().split()]
result = findMatrix(nums)
print(result)    
    
