# Link:- https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-sub-array-with-sum-k


# Time complexity: O(n^2)
def longest_subarray_with_sum_k_positive_negative_zeros(arr,k):
    n = len(arr)
    sum_dict = {} # key: prefix_sum, value: index
    prefix_sum = 0
    max_len = 0
    for i in range(n):
        prefix_sum+=arr[i]
        if prefix_sum == k:
            max_len = max(max_len, i+1)

        # not checkng for sum-k value in sum dict, if present then we can consider the array from last occurrent of the complement to the current value as one more candiate to have max_len_subarray with sum k
        complement = prefix_sum - k
        if complement in sum_dict:
            max_len = max(max_len, i-sum_dict[complement])
        
        # Since we are findding the longest subarray so we should not update the value of the sum in the sum_dict if it is already present otherwise we will not get the longest subarray and instead get the length of the shortest subarray
        if prefix_sum not in sum_dict:
            sum_dict[prefix_sum] = i
    return max_len


arr = [10, 5, 2, 7, 1, 9]
k = 15
print(longest_subarray_with_sum_k_positive_negative_zeros(arr,k)) # 4