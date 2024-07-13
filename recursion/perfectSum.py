# link:- https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=perfect-sum-problem

# approach-1: Take and Not Take Approach | Time Complexity:- O(2^n)
def helper(arr, n, sum, curr_sum, count, idx):
    if idx>=n:
         if curr_sum == sum:
              count[0]+=1
              return
         return
    if curr_sum > sum:
         return
        
    # Take case
    helper(arr, n, sum, curr_sum+arr[idx], count, idx+1)
        
    # Not Take Case
    helper(arr, n, sum, curr_sum, count, idx+1)
        
    return

def perfectSum(arr, n, sum):
      count = [0]
      idx = 0
      helper(arr, n, sum, 0, count, idx)
      return count[0]

n = 6 
arr = [5, 2, 3, 10, 6, 8] 
sum = 10

print(perfectSum(arr, n, sum))