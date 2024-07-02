def getLargestPower2(n):
    power = 0
    while (1 << power) <= n:
            power+=1
    return power-1
            
        
def countSetBits(n):
    if n == 0:
        return 0
    x = getLargestPower2(n)
    
    # because if the x == 0, that means we have no power of 2 number bfore, which means value is less than 1 or we can consider 
    # it as 1. So in case of binary of 1 there's only 1 set bit, so return 1 directly.
    # Without the following edge case we will get "ValueError: negative shift count" as it will try to find 2 raise to power -1 using left shift operator which can't be done in python.
    if x == 0: # Edge case (Only in case of n is odd we need this edge case)
         return 1
    
    bitsTill2x = x * (1 << (x-1))
    mostSignificantSetBits_remaining = n - (1 << x) + 1
    remaining = n - (1 << x)
    ans = bitsTill2x + mostSignificantSetBits_remaining + countSetBits(remaining)
    return ans


n = 7
print(countSetBits(n))