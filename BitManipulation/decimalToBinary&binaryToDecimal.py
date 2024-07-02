def decToBin(num: int)->str:
    res = ""
    while(num>0):
        remainder = num%2
        res+=str(remainder)
        num = num//2
    return res[::-1]

def bin2dec(num: str)->str:
    res = 0
    power = 1
    for i in range(len(num)-1, -1, -1):
        if num[i] == '1':
            res += power
        power*=2
    return res

num = 13
d2b = decToBin(num)
print(d2b)

b2d = bin2dec(d2b)
print(b2d)



    
