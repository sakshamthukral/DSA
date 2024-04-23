from typing import List

def mergeIntervals(intervals:List[List[int]]) -> List[List[int]]:
    intervals.sort()
    ans=[]
    n = len(intervals)
    for i in range(n):
        start = intervals[i][0]
        end = intervals[i][1]
        if len(ans)!=0 and end<=ans[-1][1]:
            continue
        for j in range(i+1, n):
            if(intervals[j][0]<=end):
                end = max(end, intervals[j][1])
            else:
                break
            
        ans.append([start,end])
    return ans

intervals = [[1,4],[4,5]]
print(mergeIntervals(intervals))