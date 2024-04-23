from typing import List 

def findElement(arr:List[int], target)->int:
    n = len(arr)
    low = 0
    high = n-1
    while(low<=high):
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        
        # Note:-  One half of the array will always be sorted
        elif arr[low]<=arr[mid]:
            # Left half will be sorted
            if arr[low]<=target and target<=arr[mid]:
                high = mid-1
            else:
                low=mid+1
        else:
            # Right half will be sorted
            if arr[mid]<=target and target<=arr[high]:
                low = mid+1
            else:
                high=mid-1
    return -1

def findElementIfDuplicatesPresent(arr:List[int], target)->int:
    n = len(arr)
    low = 0
    high = n-1
    while(low<=high):
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue
        
        # Note:-  One half of the array will always be sorted
        if arr[low]<=arr[mid]:
            # Left half will be sorted
            if arr[low]<=target and target<=arr[mid]:
                high = mid-1
            else:
                low=mid+1
        else:
            # Right half will be sorted
            if arr[mid]<=target and target<=arr[high]:
                low = mid+1
            else:
                high=mid-1
    return -1


def findMinIfDuplicatesPresent(arr:List)->int:
    n=len(nums)
    low = 0
    high = n-1
    minimum=float('inf')
    while(low<=high):
        mid = (low+high)//2
        print(f"Mid:-{mid}")
        if nums[low] == nums[mid] and nums[mid] == nums[high]:
            if nums[mid] < minimum:
                minimum = nums[mid]
            low+=1
            high-=1
            continue
        if nums[low]<=nums[mid]:
            # Left half is sorted
            if nums[low]<minimum:
                minimum = nums[low]
            low=mid+1
        else:
            # Left half is sorted
            if nums[mid]<minimum:
                minimum = nums[mid]
            high=mid-1
            
    return minimum




print("Input nums",end=": ")
nums = [int(ele) for ele in input().split()]
# print("Input target",end=": ")
# target = int(input())
# index = findElement(nums,target)
# index = findElementIfDuplicatesPresent(nums,target)
minimum = findMinIfDuplicatesPresent(nums)
print(minimum)

    