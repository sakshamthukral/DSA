# Problem Link:- https://leetcode.com/problems/01-matrix/description/
from typing import List
from collections import deque
def updateMatrixBFS(mat: List[List[int]]) -> List[List[int]]:
    rows = len(mat)
    cols = len(mat[0])
    # Initialiezed 2 2d arrays visited and distance. Could have used mat array itself instead of explicityly creating visited array but it's alway suggested not to alter the given data.
    visited = [[0 for j in range(cols)] for i in range(rows)] 
    distance = [[0 for j in range(cols)] for i in range(rows)]

    q = deque()
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                q.append((i, j, 0))
                visited[i][j] = 1
                distance[i][j] = 0
    
    delta_rows = [-1, 0, 1, 0]
    delta_cols = [0, 1, 0, -1]
    while len(q)!=0:
        ele = q.popleft()
        row, col, d = ele[0], ele[1], ele[2]
        for i in range(4):
            neighbor_row = row+delta_rows[i]
            neighbor_col = col+delta_cols[i]
            if neighbor_row >= 0 and neighbor_row < rows and neighbor_col >=0 and neighbor_col<cols and visited[neighbor_row][neighbor_col] != 1:
                distance[neighbor_row][neighbor_col] = d+1
                q.append((neighbor_row, neighbor_col, d+1))
                visited[neighbor_row][neighbor_col] = 1
    return distance

n = int(input())
mat = [list(map(int, input().split())) for i in range(n)]
distance_mat = updateMatrixBFS(mat)
print(distance_mat)

        

