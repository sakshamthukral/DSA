# Problem Link:- https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=detect-cycle-in-an-undirected-graph

# This problem can be solved in 2 different approaches: 1. BFS and 2. DFS
from typing import List
from Graph import Graph
from collections import deque
def BFS(node, visited, adj):
    q = deque()
    q.append((node, -1))
    visited[node] = 1
    while len(q)!=0:
        curr_node = q.popleft()
        node_val, parent_node = curr_node[0], curr_node[1]
        for neighbour in adj[node_val]:
            if visited[neighbour] == 0:
                visited[neighbour] = 1
                q.append((neighbour, node_val))
            elif neighbour!=parent_node: # automatically visited[neighbour] == 1 condition, so no need to write this condition again
                return True
    return False

def DFS(node, visited, adj, parent):
    visited[node] = 1
    for neighbour in adj[node]:
        if visited[neighbour] == 0:
            if DFS(neighbour, visited, adj, node) == True:
                return True
        elif neighbour!=parent:
            return True
    return False
    

def isCycle(V: int, adj: List[List[int]]) -> bool:
    visited = [0]*V
    for i in range(len(visited)):
        if visited[i] == 0:
            # res = BFS(i, visited, adj)
            parent = -1
            res = DFS(i, visited, adj, parent)
            if res == True:
                return res
    return False


g = Graph()
graph = g.undirectedListInput()
V = graph[0]
adjList = graph[1]
print(isCycle(V, adjList))
