def maximumMeetings(n,start,end):
        # code here
        meetings = list(zip(start, end))
        print(meetings)
        # meetings.sort(key = lambda x: x[1])
        
        # finishTime = meetings[0][1]
        # count = 1
        # for i in range(1, len(meetings)):
        #     if meetings[i][0] > finishTime:
        #         count+=1
        #         finishTime = meetings[i][1]
        # return count

start = [1,3,0,5,8,5]
end = [2,4,6,7,9,9]
n = 6
print(maximumMeetings(n,start,end)) # sample output: 4