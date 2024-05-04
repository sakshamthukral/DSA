from typing import List

def selectionSort(arr: List[int]) -> None: 
    # Select the minimum and swap
    n = len(arr)
    for i in range(0, n):
        mini = i
        for j in range(i, n):
            if arr[j]<arr[mini]:
                mini = j
        
        # swap i with mini
        temp = arr[i]
        arr[i] = arr[mini]
        arr[mini] = temp
        
arr = [64, 25, 12, 22, 11]
selectionSort(arr)