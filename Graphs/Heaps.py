import heapq

# Your initial list of tuples
li = [(0,0), (7,3), (9,5), (4,1), (4,2), (10,5), (8,5)]

# Transform the list into a heap
heapq.heapify(li)

# Pop elements from the heap to get them in sorted order
sorted_list = [heapq.heappop(li) for _ in range(len(li))]

print(sorted_list)
