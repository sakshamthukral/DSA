def minWindow(s:str, t:str)->str:
    if t == "":
        return ""
    
    #1: Create 2 hashmaps window and countT
    window,countT = {},{}
    for char in t:
        countT[char] = 1+countT.get(char,0)
    
    have,need = 0, len(countT)
    res,resLen = "",float("inf")

    left = 0
    for right in range(len(s)):
        char = s[right]
        if s[right] in countT:
            window[char] = 1+window.get(char,0)
            if window[char] == countT[char]:
                have+=1

        while have == need:
            if right-left+1 < resLen:
                resLen = right-left+1
                res = s[left:right+1]
            
            if s[left] in countT:
                window[s[left]]-=1
                if window[s[left]]<countT[s[left]]:
                    have-=1
            left+=1
    return res if resLen!=float("inf") else ""


s = input()
t = input()
print(minWindow(s,t))