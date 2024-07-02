def myPow(x: float, n: int) -> float:
    power = n
    ans = 1
    if power < 0:
        power*=-1
    while(power>0):
        if power % 2 == 1: 
            ans = ans * x # ans will only be changed when the power is odd
            power = power - 1
        else: # if the power is even, then change x to x*x and divide power by 2, no change in the answer
            x = x * x
            power = power/2
    if n < 0:
        return 1/ans
    else:
        return ans
        
x = 2
n = 10
print(myPow(x,n))