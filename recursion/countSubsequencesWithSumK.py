def helper(arr, n, sum, index, curr_sum, count):
	if index >= n:
		if curr_sum == sum:
			count[0]+=1
		return
	helper(arr, n, sum, index+1, curr_sum+arr[index], count)
	helper(arr, n, sum, index+1, curr_sum, count)
	   
def perfectSum(arr, n, sum):
		# code here
		count = [0]
		helper(arr, n, sum, 0, 0, count)
		return count[0]

N = 6
arr = [5, 2, 3, 10, 6, 8]
sum = 10
print(perfectSum(arr, N, sum))