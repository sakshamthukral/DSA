def maxLengthBetweenEqualCharacters(s:str):
    firstOccurenceIndex = {}
    maxLen = -1
    for i in range(len(s)):
        if s[i] in firstOccurenceIndex.keys():
            subStringLen = i-firstOccurenceIndex[s[i]]-1
            if subStringLen>maxLen:
                maxLen = subStringLen
        else:
            firstOccurenceIndex[s[i]] = i
    return maxLen

s = input()
print(maxLengthBetweenEqualCharacters(s))
