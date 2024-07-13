# Link:-https://leetcode.com/problems/is-graph-bipartite/description/

# 2 Approachches:- 1. BFS, 2. DFS
from typing import List
from collections import deque
from Graph import Graph

# Assuming 2 colors tobe 0 and 1

def BFS(node, graph, node_colors):
    q = deque()
    q.append(node)
    node_colors[node] = 0 # giving starting node as color 0
    while len(q)!=0:
        current_node = q.popleft()
        current_color = node_colors[current_node]
        next_color = 1-current_color
        for neighbour in graph[current_node]:
            if node_colors[neighbour] == -1:
                node_colors[neighbour] = next_color
                q.append(neighbour)
            elif node_colors[neighbour]!=next_color:
                return False
    return True

def DFS(curr_node, curr_color, graph, node_colors):
    node_colors[curr_node] = curr_color
    for neighbour in graph[curr_node]:
        if node_colors[neighbour] == -1:
            if DFS(neighbour, 1-curr_color, graph, node_colors) == False:
                return False
            
        # if the neighbouring node is already colored and that to with the color of the curr_node that means it is not a bipartite graph and directly return a False from here.
        elif node_colors[neighbour] == curr_color: 
            return False
    return True

def isBipartite(graph: List[List[int]]) -> bool:
    node_colors = [-1]*len(graph)
    for i in range(len(graph)):
        if node_colors[i] == -1:
            # if BFS(i, graph, node_colors) == False:
            #     return False
            if DFS(i, 0, graph, node_colors) == False:
                return False
    return True

g = Graph()
g_input = g.undirectedListInput()
vertices, graph = g_input[0], g_input[1]
print(graph)
print(isBipartite(graph))