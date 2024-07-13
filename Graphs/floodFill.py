# Problem:- https://leetcode.com/problems/flood-fill/
# Approach: This problem can be solved using both BFS and DFS approaches
from typing import List
from collections import deque
def bfs(sr, sc, image, color, originalColor):
    if color == originalColor:
        return
    q = deque()
    image[sr][sc] = color
    q.append((sr, sc))
    delta_rows = [-1, 0, 1, 0]
    delta_cols = [0, 1, 0, -1]
    while len(q)!= 0:
        pixel = q.popleft()
        row = pixel[0]
        col = pixel[1]
        
        for i in range(4):
            neighbour_row = row+delta_rows[i]
            neighbour_col = col+delta_cols[i]
            if neighbour_row >=0 and neighbour_row < len(image) and neighbour_col >= 0 and neighbour_col<len(image[0]) and image[neighbour_row][neighbour_col] == originalColor:
                image[neighbour_row][neighbour_col] = color
                q.append((neighbour_row, neighbour_col))

def dfs(sr, sc, image, color, originalColor):
    if color == originalColor: # this edge case is important, else the code will go in an infinite loop
        return
    image[sr][sc] = color
    delta_rows = [-1, 0, 1, 0]
    delta_cols = [0, 1, 0, -1]

    for i in range(4):
        neighbour_row = sr+delta_rows[i]
        neighbour_col = sc+delta_cols[i]
        if neighbour_row >=0 and neighbour_row < len(image) and neighbour_col >= 0 and neighbour_col<len(image[0]) and image[neighbour_row][neighbour_col] == originalColor:
            dfs(neighbour_row, neighbour_col, image, color, originalColor)
        
 
def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    # visited = [[0 for j in range(len(image[0]))] for i in range(len(image))]
    originalColor = image[sr][sc]
    print(originalColor)
    # dfs(sr, sc, image, color, originalColor)
    bfs(sr, sc, image, color, originalColor)
    return image


vals = list(map(int,input().split()))
sr, sc, color = vals[0], vals[1], vals[2]
n = int(input())
image = [list(map(int, input().split())) for i in range(n)]
# print(image)
resultantImage = floodFill(image, sr, sc, color)
print(resultantImage)