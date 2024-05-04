def get_sum_of_divisors(n: int) -> int:
    sum_val = 0
    for i in range(1,(n//2)+1):
        if n%i == 0:
            sum_val+=i
    return sum_val+n
def sumOfAllDivisors(n: int) -> int:
    # Write your code here
    total = 0
    for i in range(1,n+1):
        total+=get_sum_of_divisors(i)
    return total

print(sumOfAllDivisors(5)) # 12