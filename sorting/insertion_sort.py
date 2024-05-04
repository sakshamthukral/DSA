def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while(j>0 and arr[j]<arr[j-1]):
            # swap
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j-=1
    return arr

arr = [64, 25, 12, 22, 11]
print(insertionSort(arr)) # [11, 12, 22, 25, 64]