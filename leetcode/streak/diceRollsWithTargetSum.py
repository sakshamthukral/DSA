from typing import List
def solve(dices:int,faces:int,target:int, dp:List[List[int]])->int:
    # base cases
    if target<0:
        return 0
    if dices==0 and target!=0:
        return 0
    if dices!=0 and target==0:
        return 0
    if dices == 0 and target == 0:
        return 1
    if dp[dices][target]!=-1:
        return dp[dices][target]
    possible_ways = 0

    for i in range(1,faces+1):
        possible_ways += solve(dices-1,faces,target-i,dp)
    
    dp[dices][target] = possible_ways
    return possible_ways
def diceRolls(dices, faces, target):
    rows = dices+1
    columns = target+1
    dp = [[-1]*columns for _ in range(rows)] # since 2 variable will be affected during recursion so we will create a 2d array 
    print(dp)
    return solve(dices,faces, target, dp)

def diceRollsBottomUp(d, f, t):
    rows = d+1
    columns = t+1
    dp = [[0]*columns for _ in range(rows)]
    dp[0][0]=1
    
    for dice in range(1,d+1):
        for target in range(1, t+1):
            ans = 0
            for i in range(1,f+1):
                if target-i>=0:
                    ans = ans+dp[dice-1][target-i]
            dp[dice][target] = ans
    return dp[d][t]


dices = int(input())
faces = int(input())
target = int(input())
print(diceRolls(dices,faces,target))
print(diceRollsBottomUp(dices,faces,target))


    