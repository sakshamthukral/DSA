from typing import List

# Brute Force Approach
def helper_brute(candidates, target, index, subsequence, ans):
        if index >= len(candidates):
            if target == 0:
                cand = subsequence[:]
                cand.sort()
                ans.add(tuple(cand))
            return
        
        if candidates[index] <= target:
            subsequence.append(candidates[index])
            helper_brute(candidates, target-candidates[index], index+1, subsequence, ans)
            subsequence.pop()
        helper_brute(candidates, target, index+1, subsequence, ans) 
def combinationSum2_brute(candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        index = 0
        subsequence = []
        helper_brute(candidates, target, index, subsequence, ans)
        return list(ans)

# ----------------------------------------------------------------------------------------------------------
# Optimal Approach

def helper_optimized(candidates, target, index, subsequence, ans):
      # since my index can never cross the length of the array, so if target becomes 0, then it means that I have found the subsequence and we need not to check for condition index >= len(candidates) as we did in the brute force approach
      if target == 0: 
            ans.append(subsequence[:])
            return
      for i in range(index, len(candidates)):
            if i>index and candidates[i] == candidates[i-1]:
                  continue
            if candidates[i] > target:
                  break
            subsequence.append(candidates[i])
            helper_optimized(candidates, target-candidates[i], i+1, subsequence, ans)
            subsequence.pop() 
                  
def combinationSum2_optimized(candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        index = 0
        candidates.sort()
        subsequence = []
        helper_optimized(candidates, target, index, subsequence, ans)
        return ans

candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum2_brute(candidates, target))
print(combinationSum2_optimized(candidates, target))