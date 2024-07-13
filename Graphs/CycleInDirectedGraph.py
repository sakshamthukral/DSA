# Problem:- https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
from Graph import Graph
from typing import List
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

def isCyclic(V : int , adj : List[List[int]]) -> bool :
    visited = [0]*V
    path = [0]*V
    for i in range(V):
        if visited[i]==0:
            if checkCycleDFS(i, adj, visited, path) == True:
                return True
    return False

g = Graph()
V, graph = g.directedListInput()
print(isCyclic(V, graph))