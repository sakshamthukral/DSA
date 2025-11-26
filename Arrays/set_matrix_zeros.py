from typing import List
def setZeroes1(matrix: List[List[int]]):
    rows = len(matrix)
    cols = len(matrix[0])
    # traverse over the matric and change -1 to 0 in tracking matrix wherever we find a 0 value
    tracking_matrix = [[-1 for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                tracking_matrix[i][j] = 0
    
    for i in range(rows):
        for j in range(cols):
            if tracking_matrix[i][j] == 0:
                for k in range(rows):
                    matrix[k][j] = 0
                for l in range(cols):
                    matrix[i][l] = 0
    return matrix
# Time Complexity: O(M.N.(M+N)) # M-> Number of rows, N-> number of cols, Worst case (all m·n cells are zero), thats why multiple M.N with (M+N) too.
# Space Complexity: O(MxN)

def setZeroes2(matrix: List[List[int]]):
    rows = len(matrix)
    cols = len(matrix[0])
    zero_indices = []
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_indices.append([i, j])
    
    for k in range(len(zero_indices)):
        index = zero_indices[k]
        row=index[0]
        col=index[1]
        for i in range(rows):
            matrix[i][col] = 0
        for j in range(cols):
            matrix[row][j] = 0
    return matrix
# Time Complexity: O(M.N.(M+N)) # M-> Number of rows, N-> number of cols, Worst case (all m·n cells are zero), thats why multiple M.N with (M+N) too.
# Space Complexity: O(K) , where K is the number of zeroes and in worst case K=M.N i.e. all zeros


def setZeroes3(matrix: List[List[int]]): # Treat the 1st col as the flag column depicting if that whole row should be converted to 0 or not
    rows = len(matrix)
    cols = len(matrix[0])
    flagFirstCol = False 

    # 1: Iterate over the 1st column and check if there's any zero, and update flagFirstCol accordingly
    for i in range(rows):
        if matrix[i][0] == 0:
            flagFirstCol = True

    # 2: Iterate over the matrix leaving 1st column aside and if we get 0, update value in corresponding 0th row and 0th col to 0
    for i in range(rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    # 3: Iteratate again over the matrix leaving 1st column aside, but in reverse direction, and check condition, if thre's 0 in either it's corresponding 0th row or corresponding 0th column then convert the element to 0 else not
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, 0, -1):

            # Condition, check if there's 0 in either it's corresponding 0th row or corresponding 0th column then change the value of the current element to 0
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # 4: If the flagFirstCol, is True, that means the 1st column had a 0 in it, so change the whole 1st column to 0 as well
    if flagFirstCol == True:
        for i in range(rows):
            matrix[i][0] = 0
    return matrix
# Time Complexity: O(M.N) # M-> Number of rows, N-> number of cols
# Space Complexity: O(1)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
ans = setZeroes3(matrix)
print(ans)
