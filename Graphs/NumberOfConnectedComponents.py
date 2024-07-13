# Question:- https://www.geeksforgeeks.org/program-to-count-number-of-connected-components-in-an-undirected-graph/

# There are 2 ways of approaching this problem, using BFS and using DFS
from Graph import Graph
from typing import List
from collections import deque

def BFS(startNode, visited: List[int], edges: List[List[int]]):
    q = deque()
    q.append(startNode)
    visited[startNode] = 1
    while len(q) != 0:
        vertex = q.popleft()

        for neighbour in edges[vertex]:
            if visited[neighbour] == 0:
                visited[neighbour] = 1
                q.append(neighbour)


def DFS(startNode, visited: List[int], edges: List[List[int]]):
    for neighbour in edges[startNode]:
        if visited[neighbour] == 0:
            visited[neighbour] = 1
            DFS(neighbour, visited, edges)

def countConnectedComponents(nVertices: int, edges: List[List[int]]):
    count = 0
    visited = [0]*nVertices
    for i in range(nVertices):
        if visited[i] == 0:
            count+=1
            # BFS(i, visited, edges) # Approach 1: Using BFS
            DFS(i, visited, edges) # Approach 2: Using DFS
    return count


g = Graph()
graph = g.undirectedListInput()
nodes = graph[0]
edges = graph[1]
print(countConnectedComponents(nodes, edges))