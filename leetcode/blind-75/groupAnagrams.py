from typing import List
def groupAnagrams(strs:List[str])->List[str]:
    charFrequency_string = {}
    for s in strs:
        count = [0]*26
        for character in s:
            index = ord(character)-ord("a") # Substracting ascii value "a" from ascii value of character to get the index 
            count[index] +=1
        
        val_lis = charFrequency_string.get(tuple(count),0)
        if val_lis:
            charFrequency_string[tuple(count)].append(s)
        else:
            charFrequency_string[tuple(count)]=[s]

    return charFrequency_string.values()

strs = [ele for ele in input().split()]
print(groupAnagrams(strs))