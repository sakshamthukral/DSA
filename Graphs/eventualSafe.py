# Problem Link:- https://leetcode.com/problems/find-eventual-safe-states/description/

# Crux: If a node is part of the cycle don't mark it 1 in Safe array and return. 

from Graph import Graph
from typing import List
from collections import deque

# ---------DFS Cycle Detection Method -------------------

def checkSafeNodesDFS(node, visited, path, safe, adj):
    visited[node] = 1
    path[node] = 1
    safe[node] = 0 # For every path0 we will initialize safe[node] as 0, considering we don't know as that if there's a cycle ahead in this path or not
    for neighbor in adj[node]:
        if visited[neighbor] == 0:
            if checkSafeNodesDFS(neighbor, visited, path, safe, adj) == True:
                return True
        elif path[neighbor] == 1:
            return True
    path[node] = 0
    safe[node] = 1 # if for a node we managed to reach here it means that till this node there was no cycle ahead of it specifically in this path so we marked it as 1 in the safe array
    return False
def eventualSafeNodes_DFS(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    visited = [0]*n
    path = [0]*n
    safe = [0]*n
    ans_safe_nodes = []
    for i in range(n):
        if visited[i] == 0:
            checkSafeNodesDFS(i, visited, path, safe, adj)
    for i in range(n):
        if safe[i] == 1:
            ans_safe_nodes.append(i)
    return ans_safe_nodes

# ---------BFS [Topo Sort Method] : Above DFS approach is more optimal--------------------
def eventualSafeNodes_BFS(graph: List[List[int]]) -> List[int]:
    vertices = len(graph)
    adjRev = [[] for _ in range(vertices)]
    for v in range(vertices):
        for neighbor in graph[v]:
            adjRev[neighbor].append(v)
    
    indegree = [0]*vertices
    for v in range(vertices):
        for neighbor in adjRev[v]:
            indegree[neighbor]+=1

    q = deque()
    safeNodes = []
    
    for i in range(vertices):
        if indegree[i] == 0:
            q.append(i)
    
    while len(q)!= 0:
        front = q.popleft()
        safeNodes.append(front)
        for neighbor in adjRev[front]:
            indegree[neighbor]-=1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    
    safeNodes.sort()
    return safeNodes

    
g = Graph()
V, adj = g.directedListInput()
print(eventualSafeNodes_BFS(adj)) # One way using topo sort, not optimal in compariosn to DFS approach
print(eventualSafeNodes_DFS(adj)) # more optima Optimal



