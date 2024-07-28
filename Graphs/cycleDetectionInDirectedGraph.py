# Problem:- https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
from Graph import Graph
from typing import List
from collections import deque
# DFS Approach---------------------------------------------------------
def checkCycleDFS(node, adj, visited, path)-> bool:
    visited[node] = 1
    path[node] = 1
    for neighbour in adj[node]:
        if visited[neighbour] == 0:
            if checkCycleDFS(neighbour, adj, visited, path) == True:
                return True
            
        # Means the node has already been traversed in same path
        elif path[neighbour] != 0: 
            return True
        
        # Backtracking logic:- While backtracking make path value back to 0 to check for other paths
    path[node] = 0 
    return False

def isCyclicDFS(V : int , adj : List[List[int]]) -> bool :
    visited = [0]*V
    path = [0]*V
    for i in range(V):
        if visited[i]==0:
            if checkCycleDFS(i, adj, visited, path) == True:
                return True
    return False
#---------------------------------------------------------------------------
# BFS Approach (Kahn's Algorithm)------------------------------------------------------------

def KahnsBFS(indegree, adj, V):
    q = deque()
    topo=[]
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
    
    while len(q)!=0:
        front = q.popleft()
        topo.append(front)
        for neighbor in adj[front]:
            indegree[neighbor]-=1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return topo

def isCyclicBFS(V : int , adj : List[List[int]]) -> bool :
    indegree = [0]*V
    for i in range(V):
        for v in adj[i]:
            indegree[v]+=1
    topo = KahnsBFS(indegree, adj, V)
    print(topo)
    if len(topo)!=V:
        return True
    return False
# -----------------------------------------------------------------------------------
g = Graph()
V, graph = g.directedListInput()
# print(isCyclicDFS(V, graph))
print(isCyclicBFS(V, graph))