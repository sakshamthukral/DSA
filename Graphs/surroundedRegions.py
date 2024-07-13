# Problem Link:- https://leetcode.com/problems/surrounded-regions/description/
# This problem can be solved using both BFS and DFS approach

from typing import List
from collections import deque

# Approach-1 using BFS
def bfs(node_row, node_col, b, visited, rows_delta, cols_delta):
    q = deque()
    q.append((node_row, node_col))
    visited[node_row][node_col] = 1
    while len(q)!=0:
        ele = q.popleft()
        row, col = ele[0], ele[1]
        for i in range(4):
            nr = row+rows_delta[i]
            nc = col+cols_delta[i]
            if nr >= 0 and nr < len(b) and nc>=0 and nc < len(b[0]) and b[nr][nc] == '0' and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = 1        

# Approach-2 using DFS
def dfs(node_row, node_col, b, visited, rows_delta, cols_delta):
    visited[node_row][node_col] = 1
    for i in range(4):
        nr = node_row+rows_delta[i]
        nc = node_col+cols_delta[i]
        if nr >= 0 and nr < len(b) and nc>=0 and nc < len(b[0]) and b[nr][nc] == '0' and visited[nr][nc] == 0:
            dfs(nr, nc, b, visited, rows_delta, cols_delta)
    
def solve(board: List[List[str]]) -> None:
    rows = len(board)
    cols = len(board[0])
    b = [row[:] for row in board]
    visited = [[0 for j in range(cols)] for i in range(rows)]
    rows_delta = [-1, 0, 1, 0]
    cols_delta = [0, 1, 0, -1]

    # Traversing over first and last row (i.e. boundary rows)
    for j in range(cols):
        if b[0][j] == '0':
            # bfs(0, j, b, visited, rows_delta, cols_delta)
            dfs(0, j, b, visited, rows_delta, cols_delta)
        
        if b[rows-1][j] == '0':
            # bfs(rows-1, j, b, visited, rows_delta, cols_delta)
            dfs(rows-1, j, b, visited, rows_delta, cols_delta)
    
    # Traversing over first and last column (i.e. boundary columns)
    for i in range(rows):
        if b[i][0] == '0':
            # bfs(i, 0, b, visited, rows_delta, cols_delta)
            dfs(i, 0, b, visited, rows_delta, cols_delta)
        
        if b[i][cols-1] == '0':
            # bfs(i, cols-1, b, visited, rows_delta, cols_delta)
            dfs(i, cols-1, b, visited, rows_delta, cols_delta)
    
    # Till this step all the '0's connected in any manner to the boundary will get visited and only the '0's not connected to boundaries will stay non-visited. So now we can simply iterate and mark every '0' which is not-earlier visited to 'X'
    for i in range(rows):
        for j in range(cols):
            if b[i][j] == '0' and visited[i][j] == 0:
                b[i][j] = 'X'
    return b

n = int(input())
board = [input().split() for i in range(n)]

b = solve(board)
print(b)