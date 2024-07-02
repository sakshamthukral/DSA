
def move_zeros(arr):
    n = len(arr)
    zero_ptr = -1
   
    while arr[zero_ptr]!=0:
        zero_ptr+=1
    for i in range(zero_ptr+1,n):
        if arr[i]!=0:
            arr[zero_ptr] = arr[i]
            arr[i] = 0
            zero_ptr+=1
    return arr


arr = [0,1,0,3,12]
print(move_zeros(arr)) # [1, 3, 12, 0, 0]

        
