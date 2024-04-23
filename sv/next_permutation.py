from typing import List

def reverse_arr(arr:List[int], start:int, end:int)->List[int]:
    while (start<end):
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1
    return arr

def get_next_permutation(arr:List[int])->List[int]:
    n = len(arr)
    if (n==1):
        return
    break_point = -1 
    for i in range(n-2,-1,-1): 
        if (arr[i]<arr[i+1]):
            break_point = i 
            break
    if (break_point == -1): 
        reverse_arr(arr,0,n-1)
        return 
    for j in range(n-1,break_point,-1):
        if(arr[j]>arr[break_point]):
            arr[break_point],arr[j] = arr[j],arr[break_point]
            break
    print(arr)
    print(break_point)
    print(n)
    reverse_arr(arr,break_point+1,n-1)
    return 
             
          

arr = [1,3,2]
get_next_permutation(arr)
print(arr)