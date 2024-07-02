def countSubsequences(s, curr_str, n, index, subsequences):
        if index >= n:
            if curr_str!="":
                 subsequences.add(curr_str)
            return 0
        countSubsequences(s, curr_str+s[index], n, index+1, subsequences)
        countSubsequences(s, curr_str, n, index+1, subsequences)
def betterString(str1, str2):
        # Code here
        subsequences1 = set()
        subsequences2 = set()
        
        countSubsequences(str1, "", len(str1), 0, subsequences1)
        countSubsequences(str2, "", len(str2), 0, subsequences2)

        if len(subsequences1) > len(subsequences2):
           return str1
        else:
           return str2

print(betterString("gfg","ggg"))