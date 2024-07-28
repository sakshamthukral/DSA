# Problem Link:- https://leetcode.com/problems/course-schedule-ii/submissions/1322224845/
from typing import List
from collections import deque
# This problem can be solved using 2 approaches:-

# 1. DFS Approach: Find the topo sort of the graph while checking if there exists a cycle in the graph. If cycle exists then we can't form a course schedule so return false, else return True. In the main trigger function if the cycleDetectTopo return false then return empty list [] else return the topological sort sequence.
#  2. BFS Approach (Preffered Apprach): Using Kahn's Algorithm, try to find the topolofical sort sequence of the graph, if there exists a cycle, then length of topo sort sequence will not be equal to the numCourses (number of vertices) as all the vertices won't be iterated, so we will return False in this case, else if len(topo Sort) == numCourses then return True, depicted yes there exists a topological sequence for the course schedules.

# -----------------DFS Apprach (Not So intuitive -----------------------------
# Creating Adjacency list
def createAdj(numCourses, prerequisites) -> List[List[int]]:
    adj = [[] for i in range(numCourses)]
    for courses in prerequisites:
        adj[courses[1]].append(courses[0])
    return adj

def dfs(node, visited, pathVisited, adj, stack):
    visited[node] = 1
    pathVisited[node] = 1
    for neighbor in adj[node]:
        if visited[neighbor] == 0:
            if dfs(neighbor, visited, pathVisited, adj, stack) == True:
                return True
        elif pathVisited[neighbor] == 1:
            return True
    stack.append(node)
    pathVisited[node] = 0
    return False
def DFS_topo(numCourses, adj):
    visited = [0]*numCourses
    pathVisited = [0]*numCourses
    stack = []
    for i in range(numCourses):
        if visited[i] == 0:
            if dfs(i, visited, pathVisited, adj, stack) == True: # cycle exists
                print("Returning empty list")
                return []
    topo = []
    for i in range(numCourses):
        topo.append(stack.pop())
    return topo
# ------------------------------------------------------------
# ----------------BFS Approach(Prefferd Approach)----------------
# BFS Approach (finding topo sort)
def BFS_topo(numCourses, adj):
    indegree = [0]*numCourses
    topo = []
    for i in range(numCourses):
        for v in adj[i]:
            indegree[v]+=1

    q = deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            q.append(i)
    
    while len(q)!=0:
        front = q.popleft()
        topo.append(front)
        for neighbor in adj[front]:
            indegree[neighbor]-=1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return topo
# --------------------------------------------
def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    adj = createAdj(numCourses, prerequisites)
    # BFS
    topo = BFS_topo(numCourses, adj)

    if len(topo) != numCourses:
        return []
    return topo

    # DFS Approach
    # return DFS_topo(numCourses, adj)

numCourses = 2
prerequisites = [[0,1],[1,0]]
print(findOrder(numCourses, prerequisites))