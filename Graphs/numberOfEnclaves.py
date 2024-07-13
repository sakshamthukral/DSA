# Problem:-https://leetcode.com/problems/number-of-enclaves/description/

# This problem can be solved using both BFS and DFS approach, and have solved the problem using both approaches below

from typing import List
from collections import deque

def bfs(node_row, node_col, grid, visited, delta_row, delta_col):
    q = deque()
    q.append((node_row, node_col))
    visited[node_row][node_col] = 1
    while len(q)!=0:
        node = q.popleft()
        row, col = node[0], node[1]
        for i in range(4):
            nr = row+delta_row[i]
            nc = col+delta_col[i]
            if nr>=0 and nr<len(grid) and nc>=0 and nc<len(grid[0]) and grid[nr][nc] == 1 and visited[nr][nc] == 0:
                q.append((nr,nc))
                visited[nr][nc] = 1

def dfs(node_row, node_col, grid, visited, delta_row, delta_col):
    visited[node_row][node_col] = 1
    for i in range(4):
        nr = node_row+delta_row[i]
        nc = node_col+delta_col[i]
        if nr>=0 and nr<len(grid) and nc>=0 and nc<len(grid[0]) and grid[nr][nc] == 1 and visited[nr][nc] == 0:
            dfs(nr, nc, grid, visited, delta_row, delta_col)

def numEnclaves(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    visited = [[0 for j in range(cols)] for i in range(rows)]
    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]

    # Iterating over the 1st and last row
    for j in range(cols):
        if grid[0][j] == 1:
            bfs(0, j, grid, visited, delta_row, delta_col)
            # dfs(0, j, grid, visited, delta_row, delta_col)
            
        if grid[rows-1][j] == 1:
            bfs(rows-1, j, grid, visited, delta_row, delta_col)
            # dfs(rows-1, j, grid, visited, delta_row, delta_col)
    # Iterating over the 1st and last col
    for i in range(rows):
        if grid[i][0] == 1:
            bfs(i, 0, grid, visited, delta_row, delta_col)
            # dfs(i, 0, grid, visited, delta_row, delta_col)
        if grid[i][cols-1] == 1:
            bfs(i, cols-1, grid, visited, delta_row, delta_col)
            # dfs(i, cols-1, grid, visited, delta_row, delta_col)
            
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and visited[i][j] == 0:
                count+=1
    return count

n = int(input())
grid = [list(map(int,input().split())) for i in range(n)]
ans = numEnclaves(grid)
print(ans)

