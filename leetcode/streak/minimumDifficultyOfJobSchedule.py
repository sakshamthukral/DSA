from typing import List

def minDifficulty1(jobDifficulty:List[int],d:int)->int:
    if len(jobDifficulty)<d:
        return -1
    cache = {} # for inducting memorization
    def dfs(idx, d, curMaxDifficulty):
        # Base case-1
        if idx == len(jobDifficulty):
            return 0 if d==0 else float("inf") # because the case in which d is not 0, but we have already iterated over all the jobs, it is an invalid case, in order for our logic to ignore the result of this invalid case we are passing the max value possible
        # base case-2
        if d == 0:
            return float("inf") # because the case in which d becomes 0 and there are still jobs left to consider in the array it is an invalid case, in order for our logic to ignore the result of this invalid case we are passing the max value possible
        
        if (idx, d, curMaxDifficulty) in cache:
            return cache[(idx, d, curMaxDifficulty)]   
        
        curMaxDifficulty = max(curMaxDifficulty, jobDifficulty[idx])

        difficultyOnSameDay = dfs(idx+1, d, curMaxDifficulty) # case where we will continue the day with more jobs
        totalDifficultyTillNewDay = curMaxDifficulty+dfs(idx+1, d-1, -1) # case where we will end the day. sending curMaxDifficulty as -1 because new day will start now and therefore we need max value from new day 
        
        cache[(idx, d, curMaxDifficulty)] = res = min(difficultyOnSameDay, totalDifficultyTillNewDay)
        return res

    return dfs(0, d, -1)


def minDifficulty2_Helper_dfs(jobDifficulty:List[int],d:int,idx,dp)->int:
    # base case
    if d == 1:
        return max(jobDifficulty[idx:])
    if dp[d][idx] != -1:
        return dp[d][idx]
    
    curMaxDifficulty = 0
    res = float("inf")

    for i in range(idx, len(jobDifficulty)-d+1):
        curMaxDifficulty = max(curMaxDifficulty, jobDifficulty[i])
        res = min(res, curMaxDifficulty+minDifficulty2_Helper_dfs(jobDifficulty, d-1, idx+i+1,dp))
    dp[d][idx] = res
    return res

def minDifficulty2(jobDifficulty:List[int],d:int)->int:
    if len(jobDifficulty)<d:
        return -1
    rows = d+1 # number of days.Planned to keep day 0th row as all -1's always
    columns = len(jobDifficulty) # Again keeping 0th column as all -1's always
    dp = [[-1]*columns for _ in range(rows)] # keeping all values as -1 initially because as per constraint the jobDifficulty value in array can also be 0
    idx = 0
    return minDifficulty2_Helper_dfs(jobDifficulty, d, idx, dp)



jobDifficulty = [int(ele) for ele in input().split()]
d = int(input())
print(minDifficulty1(jobDifficulty,d))
print(minDifficulty2(jobDifficulty,d))