from Graph import Graph
import heapq
from queue import PriorityQueue

# Using Priority Queue directly (preffered approach to follow)

def dijkstrasShortestDistance(adj, v, source):
  dist = [float('inf')]*v
  pq = PriorityQueue()
  pq.put((0, source))
  dist[source] = 0
  while(pq.qsize()!=0):
    topEle = pq.get()
    distance, node = topEle[0], topEle[1]
    for neighbor in adj[node]:
      neighbor_node, neighbor_weight = neighbor[0], neighbor[1]
      if distance+neighbor_weight < dist[neighbor_node]:
        dist[neighbor_node] = distance+neighbor_weight
        pq.put((dist[neighbor_node], neighbor_node))
  return dist


# g = Graph()
# graph = g.weightedUndirectedListInput()
# V, adj = graph[0], graph[1] 
adj = [[(1, 9)], [(0, 9)]]
v = len(adj)
source = 0
output = dijkstrasShortestDistance(adj, v, source)
print(output)
#-----------------------------------------------------------------------
# Using Heapq library. (not preferred)
# def dijkstra(V, adj, S):
#     pq = []
#     distance = [float('inf')]*V
#     distance[S] = 0
#     heapq.heappush(pq, (0, S))
#     while pq:
#         smallest_node = heapq.heappop(pq)
#         dist = smallest_node[0]
#         node = smallest_node[1]
#         for adjacent in adj[node]:
#             edge_weight = adjacent[1]
#             adj_node = adjacent[0]
#             if dist+edge_weight < distance[adj_node]:
#                 distance[adj_node] = dist+edge_weight
#                 heapq.heappush(pq, (distance[adj_node], adj_node))
#     return distance
        

# g = Graph()
# graph = g.weightedUndirectedListInput()
# V, adjList = graph[0], graph[1] 
# V = 6
# adjList = [[(2, 4), (1, 4)], [(0, 4), (2, 2)], [(0, 4), (1, 2), (3, 3), (5, 6), (4, 1)], [(2, 3), (5, 2)], [(2, 1), (5, 3)], [(2, 6), (4, 3), (3, 2)]]
# S = 0
# res = dijkstra(V, adjList, S)
# print(res)