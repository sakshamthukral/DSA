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


def recursive_bubbleSort(arr: List[int], n):
    # adjacent swap to place the largest number at it's correct position i.e in the end
    if n == 1:
        return
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            # swap
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
    recursive_bubbleSort(arr, n-1)

    
arr = [64, 34, 25, 12, 22, 11, 90]
# bubbleSort(arr, len(arr))
recursive_bubbleSort(arr, len(arr))
print(arr) # [11, 12, 22, 25, 34, 64, 90]