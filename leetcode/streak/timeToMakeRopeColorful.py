from typing import List
def minCost(colors:str, neededTime:List[int])->int:
    minTime = 0
    i=1
    while i < len(colors):
        if colors[i-1] == colors[i]:
            currColorMinTime = []
            currColorMinTime.append(neededTime[i-1])
            consecutives = 1
            while i<len(colors) and colors[i-1] == colors[i]:
                currColorMinTime.append(neededTime[i])
                consecutives+=1
                i+=1
            currColorMinTime.sort()
            print(currColorMinTime)
            for j in range(consecutives-1):
                minTime+=currColorMinTime[j]
        else:
            i+=1
    return minTime
def minCostOptimized(colors:str, neededTime:List[int])->int:
    minTime = 0
    i=1
    while i < len(colors):
        if colors[i-1] == colors[i]:
            currColorMaxTime = 0
            currTime = neededTime[i-1]
            while i<len(colors) and colors[i-1] == colors[i]:
                currColorMaxTime = max(neededTime[i-1],neededTime[i],currColorMaxTime)
                currTime+=neededTime[i]
                i+=1
            minTime+=(currTime-currColorMaxTime) # as we are removing all consecutives, keeping only the one with highest removal time
        else:
            i+=1
    return minTime

colors = input()
neededTime = [int(time) for time in input().split()]
print(minCostOptimized(colors,neededTime))