# Question: https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

from typing import List
from queue import Queue # Instead of using Queue from queue module, we can use deque from collections module
def bfsOfGraph(V: int, adj: List[List[int]]) -> List[int]:
    # code here
    q = Queue()
    ans = []
    q.put(0)
    visited = [0]*V
    visited[0] = 1
    while q.empty() == False:
        node = q.get()
        ans.append(node)
        for neighbour in adj[node]:
            if visited[neighbour] == 0:
                visited[neighbour] = 1
                q.put(neighbour)
    return ans