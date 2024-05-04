from typing import List

# Brute Force-1
# def setZeroes1(matrix: List[List[int]])->None:
#     rows_to_zero = []
#     columns_to_zero = []
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             ele = matrix[i][j]
#             if(ele == 0):
#                 rows_to_zero.append(i)
#                 columns_to_zero.append(j)
    
#     for row in rows_to_zero:
#         for col in range(len(matrix[0])):
#             matrix[row][col] = 0
#     for col in columns_to_zero:
#         for row in range(len(matrix)):
#             matrix[row][col] = 0
 
def setZeroes(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)): # Iterating over rows
            for j in range(len(matrix[0])): # iterating over the columns
                if matrix[i][j] == 0:
                    for k in range(len(matrix)): # converting all the elements in that column to -1
                        if matrix[k][j] != 0:
                            matrix[k][j] = -1
                    for l in range(len(matrix[0])):
                        if matrix[i][l] != 0:
                            matrix[i][l] = -1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j],end=" ")
            print()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0                

# BruteForce-2
# def setZeroes2(matrix: List[List[int]])->None:
#     col0 = 1
#     rows = len(matrix)
#     columns = len(matrix[0])
#     for i in range(rows):
#         if(matrix[i][0] == 0):
#             col0=0
#         for j in range(1,columns):
#             if(matrix[i][j] == 0):
#                 matrix[0][j] = matrix[i][0] = 0
#     for i in range(rows-1,-1,-1):
#         for j in range(columns-1,0,-1):
#             if(matrix[i][0] == 0 or matrix[0][j] == 0):
#                 matrix[i][j] = 0
#         if col0 == 0:
#             matrix[i][0] = 0

# Approach-2
def set_zeros_2(matrix:List[List[int]])->None:
    flag = 1 # tracks if there's any 0 in first column of the matrix
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            flag = 0
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in range(len(matrix)-1, -1, -1):
        for j in range(len(matrix[0])-1, 0, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0: # not and, or will because either element ies in row or in the column containing 1 0 somewhere
                matrix[i][j] = 0
        if flag == 0:
            matrix[i][0]=0
    

def print_mat(matrix: List[List[int]])->None:
    for i in range(len(matrix)):
        print(matrix[i])
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# setZeroes1(matrix)
# setZeroes(matrix)
set_zeros_2(matrix)
print_mat(matrix)