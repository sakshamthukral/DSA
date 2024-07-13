class Graph:
    def __init__(self):
        pass

    def undirectedMatrixInput(self):
        nVertices, nEdges = map(int, input().split())
        adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
        for i in range(nEdges):
            v1, v2 = map(int, input().split())
            adjMatrix[v1][v2] = 1
            adjMatrix[v2][v1] = 1
        return (nVertices, adjMatrix)
    
    def directedMatrixInput(self):
        nVertices, nEdges = map(int, input().split())
        adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
        for i in range(nEdges):
            v1, v2 = map(int, input().split())
            adjMatrix[v1][v2] = 1
        return (nVertices, adjMatrix)
    
    def undirectedListInput(self):
        nVertices, nEdges = map(int, input().split())
        adjList = [[] for i in range(nVertices)]
        for i in range(nEdges):
            v1, v2 = map(int, input().split())
            adjList[v1].append(v2)
            adjList[v2].append(v1)
        return (nVertices, adjList)
    
    def directedListInput(self):
        nVertices, nEdges = map(int, input().split())
        adjList = [[] for i in range(nVertices)]
        for i in range(nEdges):
            v1, v2 = map(int, input().split())
            adjList[v1].append(v2)
        return (nVertices, adjList)


if __name__ == '__main__':
    g = Graph()
    graph = g.undirectedMatrixInput()
    print(graph, end="\n\n")
    graph2 = g.directedMatrixInput()
    print(graph2, end="\n\n")
    graph3 = g.undirectedListInput()
    print(graph3, end="\n\n")
    graph4 = g.directedListInput()
    print(graph4, end="\n\n")
