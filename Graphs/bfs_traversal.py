#User function Template for python3
# In this case we are taking Adjacency List and not Adjacency Matrix
class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsHelper(self, node, adj, visited, ans):
        ans.append(node)
        visited[node] = True
        for neighbor in adj[node]:
            if visited[neighbor] == False:
                self.dfsHelper(neighbor, adj, visited, ans)
    def dfsOfGraph(self, V, adj):
        # code here
        visited = [False]*V
        ans = []
        for i in range(V):
            if visited[i] == False:
                self.dfsHelper(0, adj, visited, ans)
        return ans

#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends