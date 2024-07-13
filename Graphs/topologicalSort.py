# Problem Link:- https://www.geeksforgeeks.org/problems/topological-sort/1

from Graph import Graph

def DFS(node, visited, adj, stack):
    visited[node] = 1
    for neighbor in adj[node]:
        if visited[neighbor] == 0:
            DFS(neighbor, visited, adj, stack)
    stack.append(node)

def topoSort(V, adj):
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


g = Graph()
V, adj = g.directedListInput()
print(topoSort(V, adj))