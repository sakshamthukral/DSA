from typing import List
def minimumArea(grid: List[List[int]]) -> int:
    min_row, max_row = float('inf'), float('-inf')
    min_col, max_col = float('inf'), float('-inf')
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                min_row = min(min_row,i)
                max_row = max(max_row,i)
                min_col = min(min_col,j)
                max_col = max(max_col,j)
    
    if min_row == float('inf'):
        return 0
    height = max_row-min_row + 1
    width = max_col-min_col + 1
    return height*width

# grid = [[0,1,0],[1,0,1]]
grid = [[0,0],[1,0]]
print(minimumArea(grid)) # 2