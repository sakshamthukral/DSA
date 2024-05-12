def rotate_array_by_one(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = temp
    return arr

def rotate_array(arr,d):
    n = len(arr)
    d = d%n
    temp = []
    for i in range(d):
        temp.append(arr[i])
    for i in range(d,n):
        arr[i-d] = arr[i]
    for i in range(d):
        arr[n-d+i] = temp[i]
    return arr

def reverse_array(arr, start, end):
    while(start<end):
        temp = start
        start = end
        end = start
        start+=1
        end-=1

def optimal_rotate_array(arr,d):
    n = len(arr)
    reverse_array(arr, 0, d-1)
    reverse_array(arr, d,n-1)
    reverse_array(arr, 0, n-1)
    return arr


# arr = [1,2,3,4]
# print(rotate_array_by_one(arr)) # [2, 3, 4, 5, 1]
arr = [1,2,3,4,5]
print(rotate_array(arr,2)) # [3, 4, 5, 1, 2]
print(optimal_rotate_array(arr,2)) # [3, 4, 5, 1, 2]