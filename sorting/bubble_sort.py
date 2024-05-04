from typing import List

def bubbleSort(arr: List[int], n: int):
    # adjacent swap to place the largest number at it's correct position i.e in the end
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                # swap
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        if swapped == False:
            break
    
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr, len(arr))