# Problem Link:- https://leetcode.com/problems/course-schedule-ii/

from typing import List
from Graph import Graph

def createAdjacencyList(numCourses, prerequisites)-> List[List[int]]:
        adj = [[] for i in range(numCourses)]
        for c in prerequisites:
            adj[c[1]].append(c[0])
        return adj
def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    adj = createAdjacencyList(numCourses, prerequisites)
    print(adj)


numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
findOrder(numCourses, prerequisites)


