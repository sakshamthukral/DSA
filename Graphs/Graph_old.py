import queue
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
    
    def addEdge(self, v1, v2):
        if v1<0 or v1 > self.nVertices or v2<0 or v2 > self.nVertices:
            return "Invalid vertices"
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2):
            self.adjMatrix[v1][v2] == 0
            self.adjMatrix[v2][v1] == 0
        else:
            return "No edge found"

    def containsEdge(self, v1, v2):
        return self.adjMatrix[v1][v2] == 1
    

    def __dfsHelper(self, sv, visited):
        print(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] == False:
                self.__dfsHelper(i, visited)

    def dfs(self, sv):
        visited = [False for i in range(self.nVertices)]
        self.__dfsHelper(sv, visited)
    
    def bfs(self, sv):
        q = queue.Queue()
        q.put(sv)
        visited = [False for i in range(self.nVertices)]
        visited[sv] = True
        while(q):
            front = q.get()
            print(front)
            for i in range(self.nVertices):
                if self.adjMatrix[front][i] > 0 and visited[i] == False:
                    q.put(i)
                    visited[i] = True

    def __str__(self):
        return str(self.adjMatrix)

g = Graph(5)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(2,4)
g.addEdge(4,1)
g.addEdge(4,3)
g.dfs(2)
print("-----------------")
g.bfs(2)

print(g)

