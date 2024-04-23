from typing import List
def makeEqual(words:List[str])->bool:
    count = {}
    n = len(words)
    for word in words:
        for character in word:
            if character in count.keys():
                count[character]+=1
            else:
                count[character]=1
    print(count)
    res = True
    for value in count.values():
        if value%n != 0:
            return False
    return res

words = [ele for ele in input().split()]
print(makeEqual(words))