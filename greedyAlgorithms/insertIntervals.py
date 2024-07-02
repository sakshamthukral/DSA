from typing import List
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Step-1 reach to the correct position where newInterval can be inserted by iterating till our intervals don't overlap with the newInterval.
        i = 0
        result = []
        while(i<len(intervals) and intervals[i][1] < newInterval[0]):
            result.append(intervals[i])
            i+=1
        # Till here we are sure that out i stands at position where the intervals[i] overlaps with newInterval
        
        # Now check/iterate all intervals till the first index of our arrays is less than the end index of the new interval as those all intervals will be the overlapping ones with the newInterval
        while(i<len(intervals) and intervals[i][0] <= newInterval[1]):
            # Update the newInterval
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i+=1
        
        # Now here our i reaches a position where our remaining intervals in array are not overlapping anymore with the newInterval
        
        # Simply put the newly updated newInterval in the results array and copy all the remaining intervals directly to the results
        result.append(newInterval)
        while(i<len(intervals)):
            result.append(intervals[i])
            i+=1
        return result

interval = [[1,3],[6,9]]
newInterval = [2,5]
print(insert(interval, newInterval)) # sample output: [[1,5],[6,9]]