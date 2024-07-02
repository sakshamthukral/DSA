def longest_subarray_sum_k(arr, k):
    left, right = 0,0
    n = len(arr)
    prefix_sum = 0
    max_len = 0
    while(right<n):
        prefix_sum+=arr[right]
        while(left<=right and prefix_sum>k):
            prefix_sum-=arr[left]
            left+=1
        if prefix_sum == k:
            max_len = max(max_len,right-left+1)
        right+=1
    return max_len

arr = [10, 5, 2, 7, 1, 9]
k = 15
print(longest_subarray_sum_k(arr,k)) # 4

        
