def getLenghtOfOptimalCompression(s:str, k:int)->int:
    cache = {}
    def count(i, k, prev, prev_cnt):
        if (i,k,prev,prev_cnt) in cache:
            return cache[(i,k,prev,prev_cnt)] 
        if k<0: # condition
            return float("inf")
        if i>=len(s): # base case
            return 0
        # case-1: if previous element is same as current element
        if s[i] == prev:
            digit_increment = 1 if prev_cnt in [1,9,99] else 0
            res = digit_increment + count(i+1, k, s[i], prev_cnt+1)
        # case-2: if previous element is not same as current element
        else:
            # case-1: decided to delete element
            countIfElementDeleted = count(i+1, k-1, prev, prev_cnt)
            # case-2: decided to keep element
            countIfElementKept = 1+count(i+1, k, s[i], 1)
            res = min(countIfElementDeleted, countIfElementKept)
        cache[(i,k,prev,prev_cnt)] = res
        return res

    return count(0, k, "", 0)

s=input()
k=int(input())
print(getLenghtOfOptimalCompression(s,k))
