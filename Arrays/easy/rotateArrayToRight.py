# Link: https://leetcode.com/problems/rotate-array/description/
from typing import List
# Approach 1: Time Complexity: O(n+d), Space Complexity: O(d)
def rotate_1(nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums

        # Put last k elements in the temp array
        temp = []
        n = len(nums)
        k = k%n
        for i in range(n-k, n):
            temp.append(nums[i])
        # Shift elements to the right
        for i in range(n-k-1, -1, -1):
            nums[i+k] = nums[i]
        # put back temp elements in the nums array
        for i in range(k):
            nums[i] = temp[i]
        return nums
# Approach 2: Time Complexity: O(2n), Space Complexity: O(1)
def reverse(arr: List[int], s: int, e: int)-> None:
     while s<e:
          temp = arr[s]
          arr[s] = arr[e]
          arr[e] = temp
          s+=1
          e-=1

    
def rotate_2(nums: List[int], k:int) -> None:
     n = len(nums)
     reverse(nums, 0, n-k-1)
     reverse(nums, n-k, n-1)
     reverse(nums, 0, n-1)


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    rotate_2(nums, k)
    print(nums)
