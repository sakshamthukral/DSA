from typing import List
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nge = [-1]*len(nums1)
        hashMap = {}
        for i in range(len(nums1)):
            hashMap[nums1[i]] = i

        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if len(stack)>0 and nums2[i] in hashMap.keys():
                nge[hashMap[nums2[i]]] = stack[-1]
            stack.append(nums2[i])
        return nge

# Time complexity: O(n)
# Space complexity: O(n)
arr1 = [4,1,2]
arr2 = [1,3,4,2]
print(nextGreaterElement(arr1, arr2)) # [-1, 3, -1]

# print(nextGreaterElement(arr1)) # [-1, 2, -1]
