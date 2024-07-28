# Problem Link:- https://leetcode.com/problems/course-schedule/description/
# This problem can be solved using 2 approaches:-
#  1. DFS Approach: Check if there exists a cycle in the graph. If cycle exists then we can't form a course schedule so return false, else return True.
#  2. BFS Approach (Preffered Apprach): Using Kahn's Algorithm, try to find the topolofical sort sequence of the graph, if there exists a cycle, then length of topo sort sequence will not be equal to the numCourses (number of vertices) as all the vertices won't be iterated, so we will return False in this case, else if len(topo Sort) == numCourses then return True, depicted yes there exists a topological sequence for the course schedules.

# Crux: If there exists a cycle, then we can never have a Topo Sort, and that would mean we can schedule the courses in that manner.

from typing import List
from collections import deque

# DFS Approach: Cycle Detection

def detectCycleHelper(node, visited, pathVisited, adj):
    visited[node] = 1
    pathVisited[node] = 1
    for neighbor in adj[node]:
        if visited[neighbor] == 0:
            if detectCycleHelper(neighbor, visited, pathVisited, adj) == True:
                return True
        elif pathVisited[neighbor] == 1:
            return True
    pathVisited[node] = 0
    return False
def detectCycle(numCourses, adj):
    visited = [0]*numCourses
    pathVisited = [0]*numCourses
    
    for i in range(numCourses):
        if visited[i] == 0:
            if detectCycleHelper(i, visited, pathVisited, adj) == True:
                return True
    
    return False


# Creating Adjacency list
def createAdj(numCourses, prerequisites) -> List[List[int]]:
    adj = [[] for i in range(numCourses)]
    for courses in prerequisites:
        adj[courses[1]].append(courses[0])
    return adj

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

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    adj = createAdj(numCourses, prerequisites)
    
    # BFS Approach (finding topo sort)
    # topo = BFS_topo(numCourses, adj)

    # if len(topo) != numCourses:
    #     return False
    # return True
    
    # If there exists a cycle then we can't schedule the courses
    if detectCycle(numCourses, adj) == True:
        return False
    else:
        return True

numCourses = 2
prerequisites = [[1,0]]
# prerequisites = [[1,0],[0,1]]
print(canFinish(numCourses, prerequisites))