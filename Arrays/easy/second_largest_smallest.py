def second_largest(arr):
    largest = arr[0]
    second_largest = -1
    for i in range(1,len(arr)):
        if arr[i]>largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i]<largest and arr[i]>second_largest: # why we are checking arr[i]<largest? Because if arr[i] is equal to larget then it is not a second largest number in the array and we need to skip it.
            second_largest = arr[i]
    return second_largest

def second_smallest(arr):
    smallest = arr[0]
    second_smallest = float('inf')
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            second_smallest = smallest
            smallest = arr[i]
        elif arr[i]>smallest and arr[i]<second_smallest: # why we are checking arr[i]>smallest? Because if arr[i] is equal to smallest then it is not a second smallest number in the array and we need to skip it.
            second_smallest = arr[i]
    return second_smallest

arr = [12, 35, 1, 10, 34, 1]
print(second_largest(arr)) # 34
print(second_smallest(arr)) # 10
