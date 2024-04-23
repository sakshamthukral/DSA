def isAnagram(s:str,t:str)->bool:
    countT = {}
    for char in s:
        countT[char] = 1+countT.get(char,0)
    for char in t:
        if char in countT:
            countT[char]-=1
        else:
            return False
    res = True
    for val in countT.values():
        if val<0 or val>0:
            res = False
    return res

s = input()
t = input()
print(isAnagram(s,t))
