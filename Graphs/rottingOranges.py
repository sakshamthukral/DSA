from collections import deque
from typing import List
def orangesRotting(grid: List[List[int]]) -> int:
  rows = len(grid)
  cols = len(grid[0])
  visited = [[0]*cols for r in range(rows)]
  
  q = deque()
  fresh_count = 0
  for i in range(rows):
    for j in range(cols):
      if grid[i][j] == 2: # the orange is rotten
        visited[i][j] = 1
        q.append((i, j, 0)) # Multi Source BFS
      if grid[i][j] == 1: # fresh orange
        fresh_count+=1  
  
  final_time = 0

  while len(q)!= 0:
    r, c, time = q.popleft()
    final_time = max(final_time, time)
    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]
    for i in range(4):
      d_row = r+delta_row[i]
      d_col = c+delta_col[i]
      if d_row >=0 and d_row < rows and d_col>=0 and d_col < cols and grid[d_row][d_col] == 1 and visited[d_row][d_col] == 0:
        visited[d_row][d_col] = 1
        fresh_count-=1
        q.append((d_row, d_col, time+1))
    
  if fresh_count == 0:
    return final_time
  else:
    return -1
    

# grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
ans = orangesRotting(grid)
print(ans)