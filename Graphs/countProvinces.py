from typing import List
from collections import deque
from Graph import Graph
# Approach 1: Using DFS , Approach 2: Using BFS

def dfs(startNode, visited, isConnected):
        visited[startNode] = 1
        for i in range(len(isConnected)):
            if isConnected[startNode][i] == 1 and visited[i] == 0:
                dfs(i, visited, isConnected)
                
def bfs(startNode, visited, isConnected):
     q = deque()
     q.append(startNode)
     visited[startNode] = 1
     while len(q) != 0:
          city = q.popleft()
          for i in range(len(isConnected)):
               if isConnected[city][i] == 1 and visited[i] == 0:
                    visited[i] = 1
                    q.append(i)
            
               
            
def countProvinces(isConnected: List[List[int]]) -> int:
        visited = [0]*len(isConnected)
        count = 0
        for i in range(0, len(visited)):
            if visited[i] == 0:
                count +=1
                dfs(i, visited, isConnected) # Approach-1
                # bfs(i, visited, isConnected) # Approach-2
        return count

g = Graph()
graph = g.undirectedMatrixInput()
cities = graph[0] # Vertices in the graph
isConnected = graph[1]
ans = countProvinces(isConnected)
print(ans)
