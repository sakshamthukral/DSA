def reverse(arr):
    i=0
    j=len(arr)-1
    while(i<j):
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1
    return arr
        
def leaders(A, N):
    #Code here
    maxi=float("-inf")
    ans=[]
    for i in range(N-1, -1, -1):
        if A[i]>=maxi:
            ans.append(A[i])
            maxi=A[i]
    return reverse(ans)

arr = [16,17,4,3,5,2]
n = 6
print(leaders(arr, n)) # [17, 5, 2]
            