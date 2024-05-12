# merge sort without using extra space


def merge(arr, l , mid, r):
    left = l
    right = mid+1
    temp = []
    while(left<=mid and right<=r):
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while(left<=mid):
        temp.append(arr[left])
        left+=1
    while(right<=r):
        temp.append(arr[right])
        right+=1
    for i in range(l, r+1):
        arr[i] = temp[i-l]
    
def mergeSort(arr, l, r):
    if l>=r:
        return
    mid = (l+r)//2
    mergeSort(arr, l, mid)
    mergeSort(arr, mid+1, r)
    merge(arr, l, mid, r)

arr = [64, 25, 12, 22, 11]
mergeSort(arr, 0, len(arr)-1)
print(arr) # [11, 12, 22, 25, 64]
