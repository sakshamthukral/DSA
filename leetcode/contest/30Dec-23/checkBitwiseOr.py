def hasTrailingZeros(nums):
    count = 0
    for ele in nums:
        bitNotation = bin(ele)
        if bitNotation[-1] == '0':
            count+=1
    if count>1:
        return True
    else:
        return False
    
nums = [int(ele) for ele in input().split()]
res = hasTrailingZeros(nums)
print(res)