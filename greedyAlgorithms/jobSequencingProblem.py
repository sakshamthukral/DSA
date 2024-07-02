class Job:
    def __init__(self, deadline = 0, profit = 0):
        self.deadline = deadline
        self.profit = profit
        self.id = 0

def JobScheduling(Jobs,n):
        
        # Step-1: Sorting based on the max profit
        Jobs.sort(key = lambda x: x.profit, reverse=True)
        
        countJobs = 0
        maxProfit = 0
        
        # Step-2: Finding the last deadline because it will help us to plan our scheduler
        lastDeadline = -1
        for job in Jobs:
            lastDeadline = max(lastDeadline, job.deadline)
        
        scheduler = [-1]*(lastDeadline+1)
        for i in range(n):
            for j in range(Jobs[i].deadline,0,-1):
                if scheduler[j]!=-1:
                    continue
                else:
                    scheduler[j] = Jobs[i].id # Putting the job id
                    countJobs+=1
                    maxProfit += Jobs[i].profit
                    break # Move to the next job after scheduling the current one
        return (countJobs, maxProfit)

# Driver code
if __name__ == '__main__':
    n = int(input("Enter the number of jobs: ")) # sample input: 4
    info = list(map(int, input("Enter the id, deadlien and profit of the jobs: ").split())) # sample input: 1 4 20 2 1 10 3 1 40 4 1 30
    Jobs = [Job() for i in range(n)]
    for i in range(n):
        Jobs[i].id = info[3*i]
        Jobs[i].deadline = info[3*i+1]
        Jobs[i].profit = info[3*i+2]
    res = JobScheduling(Jobs,n) # sample output: (2, 60)
    print("The number of jobs and the maximum profit are: ", res) # sample output: The number of jobs and the maximum profit are:  (2, 60)