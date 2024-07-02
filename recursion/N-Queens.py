from typing import List

# Approach-1
def isSafe_1(row, col, board, n):
    duprow = row
    dupcol = col

    while duprow >= 0 and dupcol >= 0: # checking left diagonally upwards
        if board[duprow][dupcol] == 'Q':
            return False
        duprow -= 1
        dupcol -= 1
    
    duprow = row
    dupcol = col
    while dupcol >= 0:
        if board[duprow][dupcol] == 'Q': # checking row in left
            return False
        dupcol -= 1
    
    duprow = row
    dupcol = col
    while duprow < n and dupcol >= 0:
        if board[duprow][dupcol] == 'Q':
            return False
        duprow += 1
        dupcol -= 1
    
    # I don't need to check in the same column, as on each isSafe as True, i move to the next column, which ensures i can never have another Q in the same column
    
    return True # So if reached till here, it means none of the condition got violated
    

def solve_1(col, board, ans, n):
    if col == n:
        ans.append(list(board))
        return
    for row in range(n):
        if isSafe_1(row, col, board, n):
            board[row] = board[row][:col]+'Q'+board[row][col+1:]
            solve_1(col+1, board, ans, n)
            board[row] = board[row][:col]+'.'+board[row][col+1:]

def solveNQueens_1(n: int) -> List[List[str]]:
    ans = []
    board = ['.'*n for _ in range(n)]
    solve_1(0, board, ans, n) # Solving column wise from left to right
    return ans
    


# Approach-2


def solve_2(col, board, ans, leftRow, upperDiagonal, lowerDiagonal, n):
    if col == n:
        ans.append(board[:])
        return
    for row in range(n):
        if leftRow[row] == 0 and lowerDiagonal[row+col] == 0 and upperDiagonal[(n-1)+(col-row)] == 0: # it true then we can place the Q at the current row and col position in board
            
            # Updating the status in hashmaps
            board[row] = board[row][:col] + 'Q' + board[row][col+1:]
            leftRow[row] = 1
            lowerDiagonal[row+col] = 1
            upperDiagonal[(n-1)+(col-row)] = 1

            solve_2(col+1, board, ans, leftRow, upperDiagonal, lowerDiagonal, n)

            # Backtracking and Updating back the status in hashmaps
            board[row] = board[row][:col] + '.' + board[row][col+1:]
            leftRow[row] = 0
            lowerDiagonal[row+col] = 0
            upperDiagonal[(n-1)+(col-row)] = 0
        

def solveNQueens_2(n: int) -> List[List[str]]:
    ans = []
    board = ['.'*n for _ in range(n)]

    # Creating 3 hashmap to hash left row elements, left-upper-diagonal elements, and left-lower-diagonal elements
    leftRow = [0]*n

    # because max sum can be (n-1)+(n-1) and therefore last index of hash should be (n-1)+(n-1). For example if n=8, largest index sum can be 7+7 = 14 (index is 1 less than actual size of the array), so hash will be of size 15, then only our last index will be 14 (0-based indexing)
    lowerDiagonal = [0]*(2*n-1)

    # because max sum can be (n-1)+(col-row) and in case row=0 and col=n-1, we will have the maximum value as (n-1)+(n-1) , therefore last index of hash should be (n-1)+(n-1). For example if n=8, largest index sum can be 7+7 = 14 (index is 1 less than actual size of the array), so hash will be of size 15, then only our last index will be 14 (0-based indexing)
    upperDiagonal = [0]*(2*n-1) 

    solve_2(0, board, ans, leftRow, upperDiagonal, lowerDiagonal, n) # Solving column wise from left to right
    return ans


n = 4
print(solveNQueens_2(n))