from typing import List

# Dutch National Flag Algorithm

def sort012(nums:List[int])->None:
    # Step-1: take 3 flags, considering everything between (0->low-1) = 0,(low->mid-1) = 1, (mid->high-1) = unsorted/random, and (high->n-1) = 2 
    low = 0
    mid = 0
    high = len(nums)-1

    # Step-2: Rules, everything between 
    # (0->low-1) = 0,
    # (low->mid-1) = 1, 
    # (mid->high-1) = unsorted/random, and 
    # (high->n-1) = 2  

    # Step-3: Conditions (while mid<=high)
    # if arr[mid] == 0 : swap(arr[low],arr[mid]), low++, mid++
    # elif arr[mid] == 1 : mid ++
    # elif arr[mid] == 2 : swap(arr[mid],arr[high]), high--

    while mid<=high:
        if(nums[mid]) == 0:
            nums[low],nums[mid] = nums[mid],nums[low]
            low+=1
            mid+=1
        elif(nums[mid] == 1):
            mid+=1
        else:
            nums[mid],nums[high] = nums[high],nums[mid]
            high-=1


nums = [2,0,2,1,1,0]
sort012(nums)
print(nums)
        



