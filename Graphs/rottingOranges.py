from typing import List
from collections import deque
def multiSourceBFS(q, oranges: List[List[int]], freshOranges) -> int:
    row_delta = [-1, 0, 1, 0]
    col_delta = [0, 1, 0, -1]
    while len(q)!=0:
        rotten = q.popleft()
        row, col = rotten[0],rotten[1]
        time = rotten[2]
        for i in range(4):
            neighbour_row = row+row_delta[i]
            neighbour_col = col+col_delta[i]
            if neighbour_row >= 0 and neighbour_row < len(oranges) and neighbour_col >=0 and neighbour_col<len(oranges[0]) and oranges[neighbour_row][neighbour_col] == 1:
                oranges[neighbour_row][neighbour_col] = 2
                freshOranges -= 1 # as we just in above line rot 1 fresh orange
                q.append((neighbour_row, neighbour_col, time+1))
    if freshOranges>0:
        return -1
    else:
        return time


def orangesRotting(grid: List[List[int]]) -> int:
    oranges = grid
    q = deque()
    freshOranges = 0
    for i in range(len(oranges)):
        for j in range(len(oranges[0])):
            if oranges[i][j] == 1:
                freshOranges += 1
            if oranges[i][j] == 2:
                q.append((i, j, 0))
    time = multiSourceBFS(q, oranges, freshOranges) # In DSA terms it will be the level of the BFS search, as in each 1 unit of team oranges at same level will get rotten

    return time

n,m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
print(orangesRotting(grid))