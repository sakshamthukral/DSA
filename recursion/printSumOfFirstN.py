from typing import List

def sumFirstN_helper(n:int,sum_val:int)->int:
    if n==0:
        return sum_val
    sum_val+=n
    return sumFirstN_helper(n-1, sum_val) # return the value returned from the recursive call not the value stored in a local variable directly to the caller
   
def sumFirstN(n: int) -> int:
    # Write your code here.
    sum_val = 0
    return sumFirstN_helper(n,sum_val)

print(sumFirstN(5)) # 15

