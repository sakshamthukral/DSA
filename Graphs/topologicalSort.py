# Problem Link:- https://www.geeksforgeeks.org/problems/topological-sort/1

from Graph import Graph
from collections import deque
# DFS Approach : Topological Sort-----------------------------
def DFS(node, visited, adj, stack):
    visited[node] = 1
    for neighbor in adj[node]:
        if visited[neighbor] == 0:
            DFS(neighbor, visited, adj, stack)
    stack.append(node)

def topoSortDFS(V, adj):
    visited = [0]*V
    stack = []
    for i in range(V):
        if visited[i] == 0:
            DFS(i, visited, adj, stack)
    ans = []
    for i in range(len(stack)):
        ele = stack.pop()
        ans.append(ele)
    return ans
#-------------------------------------------------------------


# BFS Approach : Topological Sort ----------------------------
def topsortBFS(V, adj):
    indegree = [0]*V
    topo = []
    for i in range(V):
        for v in adj[i]:
            indegree[v]+=1

    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
    
    while len(q)!=0:
        front = q.popleft()
        topo.append(front)
        for neighbour in adj[front]:
            indegree[neighbour]-=1
            if indegree[neighbour] == 0:
                q.append(neighbour)
    return topo
#--------------------------------------------------------------------

g = Graph()
V, adj = g.directedListInput()
# print(topoSortDFS(V, adj))
print(topsortBFS(V, adj))
