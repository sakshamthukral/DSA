# Approach-1: Naive approach of printing all the possible substrings and returning the lenght of longest ne with unique characters
# For getting all the substrings you can use kadan'es algorithm
#---------------------------------------------------------------
# Approach-2 :- Sliding window approach
def lengthOfLongestSubstring1(s: str) -> int:
    n = len(s)
    left = 0
    right = 0
    m = set()
    substring_length=0
    while(right<n):
        if s[right] in m:
            m.remove(s[left])
            left+=1
        else:
            m.add(s[right])
            substring_length = max(substring_length, right-left+1)
            right+=1
    return substring_length
#------------------------------------------------------------------
# Approach-3 :- Optimized Sliding window approach
def lengthOfLongestSubstring2(s: str) -> int:
    n = len(s)
    left = 0
    right = 0
    m = {}
    substring_length=0
    while(right<n):
        if s[right] in m:
            left = max(m[s[right]]+1,left)
        
        m[s[right]] = right
        substring_length = max(substring_length, right-left+1)
        right+=1
    return substring_length

s = input()
print(lengthOfLongestSubstring1(s))
print(lengthOfLongestSubstring2(s))