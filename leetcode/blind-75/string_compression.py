from typing import List
def string_compression(chars:List[str])->List[str]:
    if len(chars) <=1:
        return chars
    runner = 0
    walker = 0 # pointer for compression, which also depicts the number of characters in the compressed string
    while(runner<len(chars)):
        chars[walker] = chars[runner]
        count = 1
        while(runner+1<len(chars) and chars[runner]==chars[runner+1]):
            runner+=1
            count+=1
        if count>1:
            for val in str(count):
                walker+=1
                chars[walker]=val
        runner+=1
        walker+=1
    return walker # walker basically depicts the number of characters in the compressed string

chars = [ele for ele in input().split()]
result = string_compression(chars)
for i in range(result):
    print(chars[i],end=",")

        

        
