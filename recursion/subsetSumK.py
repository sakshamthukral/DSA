#  Problem statement
# You are given an array 'A' of 'N' integers. You have to return true if there exists a subset of elements of 'A' that sums up to 'K'. Otherwise, return false.
# Sample Input 1 :
# 4 13
# 4 3 5 2
# Sample Output 1 :
# No

# Sample Input 2 :
# 5 14
# 4 2 5 6 7
# Sample Output 2 :
# Yes




from typing import List
def helper(n, k, a, index, curr_sum) -> bool:
    if index >= n:
        if curr_sum == k:
            return True
        return False
    if helper(n, k, a, index+1, curr_sum+a[index]) == True: # Take case
        return True 
    if helper(n, k, a, index+1, curr_sum) == True: # Not Take case
        return True
    return False
def isSubsetPresent(n:int, k: int, a: List[int]) -> bool:
    # Write your code here.
    return helper(n, k, a, 0, 0)

n = 5
k = 14
a = [4, 2, 5, 6, 7]
print(isSubsetPresent(n,k,a)) 