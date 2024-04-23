from typing import List 
def findContentChildren(g:List[int], s:List[int])->int:
    i=0
    j=0
    g.sort()
    s.sort()
    while i<len(g) and j<len(s):
        child_greed = g[i]
        cookie_size = s[j]
        if child_greed<=cookie_size:
            i+=1
            j+=1
        else:
            j+=1
    return i

g = [int(ele) for ele in input().split()]
s = [int(ele) for ele in input().split()]
print(findContentChildren(g,s))