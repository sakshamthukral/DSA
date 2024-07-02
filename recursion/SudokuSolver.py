from typing import List

def isValid(board, row, col, c):
    for i in range(9):
        if board[i][col] == c:
            return False
        if board[row][i] == c:
            return False
        if board[3*(row//3)+(i//3)][3*(col//3)+i%3] == c:
            return False
    return True

def solveSudoku(board: List[List[str]]) -> None:
    rows = 9 # len(board) , in sudoku rows will always be 9
    cols = 9 # len(board[0]), in sudoku cols will always be 9
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == '.':
                for c in "123456789":
                    if isValid(board, i, j, c):
                        board[i][j] = c
                        if solveSudoku(board):
                            return True
                        else:
                            board[i][j]="."
                return False # if reached till here it means we were not able to return a solution of sudoku so return false
            
    return True # It means no more empty blocks present in the Sudoku, i.e. Sudoku solved completely so return True


board = [
        ["9", "5", "7", ".", "1", "3", ".", "8", "4"],
        ["4", "8", "3", ".", "5", "7", "1", ".", "6"],
        [".", "1", "2", ".", "4", "9", "5", "3", "7"],
        ["1", "7", ".", "3", ".", "4", "9", ".", "2"],
        ["5", ".", "4", "9", "7", ".", "3", "6", "."],
        ["3", ".", "9", "5", ".", "8", "7", ".", "1"],
        ["8", "4", "5", "7", "9", ".", "6", "1", "3"],
        [".", "9", "1", ".", "3", "6", ".", "7", "5"],
        ["7", ".", "6", "1", "8", "5", "4", ".", "9"],
    ]
print(solveSudoku(board))
print(board)
