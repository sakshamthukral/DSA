
def isPalindrome(s:str)->bool:
    s=s.lower()
    res = []
    for char in s:
        if char in "0123456789abcdefghijklmnopqrstuvwxyz":
            res.append(char)
    res = "".join(res)
    return res == res[::-1]

s = input()
print(isPalindrome(s))
