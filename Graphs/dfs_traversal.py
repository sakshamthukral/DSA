# Question: https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
def dfsHelper(startNode, visited, adj, ans):
        ans.append(startNode)
        visited[startNode] = 1
        for neighbour in adj[startNode]:
           if visited[neighbour] == 0:
                dfsHelper(neighbour, visited, adj, ans)
            
    #Function to return a list containing the DFS traversal of the graph.
def dfsOfGraph(V, adj):
        # code here
        visited = [0]*V
        ans=[]
        dfsHelper(0, visited, adj, ans)
        return ans


        