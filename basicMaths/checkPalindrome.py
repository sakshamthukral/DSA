from typing import List
def getReverse(x:int)->int:
        reverse = 0
        while(x != 0):
            last_digit = x%10
            reverse = reverse*10+last_digit
            x = x//10
        return reverse

def isPalindrome(x: int) -> bool:
    if x<0:
        return False
    else:
        reverse = getReverse(x)
        print(reverse)
        if reverse == x:
            return True
        else:
            return False
        
print(isPalindrome(121))
