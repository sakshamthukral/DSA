# problem:- https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=union-of-two-sorted-arrays

def union_of_arrays(arr1, arr2, n, m):
    union_arr = []
    ptr1,ptr2 = 0,0
    while(ptr1<n and ptr2<m):
        if arr1[ptr1]<arr2[ptr2]:
            if len(union_arr)==0 or union_arr[-1]!=arr1[ptr1]:
                union_arr.append(arr1[ptr1])
            ptr1+=1
        else:
            if len(union_arr)==0 or union_arr[-1]!=arr2[ptr2]:
                union_arr.append(arr2[ptr2])
            ptr2+=1
        
    while ptr1<n:
        if union_arr[-1]!=arr1[ptr1]:
            union_arr.append(arr1[ptr1])
        ptr1+=1
    while ptr2<m:
        if union_arr[-1]!=arr2[ptr2]:
            union_arr.append(arr2[ptr2])
        ptr2+=1
    return union_arr

arr1 = [1,2,3,4,5]
arr2 = [1,2,3]
n = len(arr1)
m = len(arr2)
print(union_of_arrays(arr1,arr2,n,m)) # [1, 2, 3, 4, 5]