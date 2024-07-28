# Problem Link:- https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=shortest-path-in-undirected-graph


from typing import List

def createAdjList(n : int, m : int, edges : List[List[int]], adjList):
    for i in range(m):
        u = edges[i][0]
        v = edges[i][1]
        weight = edges[i][2]
        adjList[u].append((v, weight))

def topoSort(node, adjList, visited, stack):
    visited[node] = 1
    for neighbor in adjList[node]:
        v = neighbor[0]
        wt = neighbor[1]
        if visited[v] == 0:
            topoSort(v, adjList, visited, stack)
    stack.append(node)
    
def shortestPath(n : int, m : int, edges : List[List[int]]) -> List[int]:
    adjList = [[] for _ in range(n)]
    createAdjList(n, m, edges, adjList)
    
    stack = []
    visited = [0]*n
    for i in range(n):
        if visited[i] == 0:
            topoSort(i, adjList, visited, stack)
    
    distance = [float('inf')]*n
    distance[0] = 0
    while len(stack) != 0:
        top = stack.pop()
        for neighbor in adjList[top]:
            v = neighbor[0]
            wt = neighbor[1]
            if distance[top]+wt < distance[v]:
                distance[v] = distance[top]+wt
    
    # If a node is not reachable then put it's ditance as -1 instead of inf (as per the question requirement)
    for i in range(len(distance)):
        if distance[i] == float('inf'):
            distance[i] = -1
    return distance


N = 6
M = 7
edge = [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
dist = shortestPath(N, M, edge)
print(dist)

