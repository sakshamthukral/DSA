def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr=[0]*(len(nums)+1)
        for ele in nums:
            arr[ele] = 1
        print(arr)
        for i in range(len(arr)):
            if arr[i] == 0:
                return i
        return -1

nums = [int(ele) for ele in input().split()]
print(missingNumber(nums))