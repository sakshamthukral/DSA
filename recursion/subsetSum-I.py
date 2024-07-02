def helper(arr, n, index, sum_res, ans):
        if index >= n:
            ans.append(sum_res)
            return
        helper(arr, n, index+1, sum_res+arr[index], ans)
        helper(arr, n, index+1, sum_res, ans)
def subsetSums(arr, n):
		# code here
		ans = []
		helper(arr, n, 0, 0, ans)
		ans.sort()
		return ans

arr = [2,3]
n = 2
print(subsetSums(arr, n))