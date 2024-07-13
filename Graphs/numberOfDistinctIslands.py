# Problem:- https://www.geeksforgeeks.org/problems/number-of-distinct-islands/0

# This problem can also be solved using either BFS approach or DFS approach. In here will be doing it with both the approaches.

from typing import List
from collections import deque

def bfs(row, col, grid, visited, delta_row, delta_col, structure):
    base_row = row
    base_col = col
    q=deque()

    q.append((row, col))
    visited[row][col] = 1
    structure.append((row-base_row, col-base_col))
    
    while len(q)!=0:
        node = q.popleft()
        r, c = node[0], node[1] # r-> row, c-> column
        for i in range(4):
            nr = r+delta_row[i] # neighbouring row
            nc = c+delta_col[i] # neighbouring column
            if nr>=0 and nr<len(grid) and nc>=0 and nc<len(grid[0]) and grid[nr][nc] == 1 and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = 1
                structure.append((nr-base_row, nc-base_col))

def dfs(row, col, grid, visited, delta_row, delta_col, structure, base_row, base_col):
    visited[row][col] = 1
    for i in range(4):
        nr = row+delta_row[i] # neighbouring row
        nc = col+delta_col[i] # neighbouring column
        if nr>=0 and nr<len(grid) and nc>=0 and nc<len(grid[0]) and grid[nr][nc] == 1 and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            structure.append((nr-base_row, nc-base_col))
            dfs(nr, nc, grid, visited, delta_row, delta_col, structure,base_row, base_col)

def countDistinctIslands(grid : List[List[int]]) -> int:
    s = set()
    rows = len(grid)
    cols = len(grid[0])
    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]
    visited = [[0 for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and visited[i][j] == 0:
                structure = []
                # bfs(i, j, grid, visited, delta_row, delta_col, structure) # Approach using BFS
                dfs(i, j, grid, visited, delta_row, delta_col, structure, i, j) # Approach using DFS
                s.add(tuple(structure))
    return len(s)


n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]

ans = countDistinctIslands(grid)
print(ans)