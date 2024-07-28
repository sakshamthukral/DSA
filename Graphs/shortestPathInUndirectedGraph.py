from collections import deque
def createAdjList(edges, n, m, adjList):
    for i in range(m):
        u,v = edges[i][0], edges[i][1]
        adjList[u].append(v)
        adjList[v].append(u)


def shortestPath(edges, n, m, src):
    adjList = [[] for _ in range(n)]
    createAdjList(edges, n, m, adjList)
    
    q = deque()
    distance = [float('inf')]*n
    distance[src] = 0
    q.append(src)
    while len(q)!=0:
        front = q.popleft()
        for neighbor in adjList[front]:
            if distance[front]+1 < distance[neighbor]:
                distance[neighbor] = distance[front]+1
                q.append(neighbor)

    for i in range(n):
        if distance[i] == float('inf'):
            distance[i] = -1
    return distance

n = 9
m= 10
edges=[[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
src=0
ans = shortestPath(edges, n, m, src)
print(ans)

