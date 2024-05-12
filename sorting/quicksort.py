
def partition(arr, low, high):
    piv = arr[low]
    i=low
    j=high
    while(i<j):
        while(arr[i]<=piv and i<=high-1):
            i+=1
        while(arr[j]>piv and j>=low+1):
            j-=1
        
        if i<j:
            # swap
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    # swap pivot with jth element
    temp = arr[j]
    arr[j] = arr[low] # pivot
    arr[low] = temp

    return j # as the pivot is at jth index


def quicksort(arr, low, high):
    if low>=high:
        return
    pivot = partition(arr, low, high)
    quicksort(arr, low, pivot-1)
    quicksort(arr, pivot+1, high)

arr = [64, 25, 12, 22, 11]
quicksort(arr, 0, len(arr)-1)
print(arr) # [11, 12, 22, 25, 64]
