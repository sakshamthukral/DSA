# Problem Type 1: Given Nth row and Mth Column, print the element in pascal triangle at position row N and column M
# Solution: To find an element at row N and col M, simplest way is to compute nCr where n=(N-1) and r=(M-1)
# Brute Force Approach
def factorial(ele):
    ans = 1
    for i in range(ele):
        ans*=(ele-i)
    return ans
def nCr(n, r): # 
    numerator = factorial(n)
    denominator = factorial(r) * factorial(n-r)
    return numerator/denominator
# Time Complexity: O(n) + O(r) + O(n-r)
# Space Complexity: O(1)
#-------------------------------------------------------------
# Optimized Approach
def optimized_nCr(n, r): # Time Complexity: O(r)
    ans = 1
    for i in range(r):
        ans = ans * (n-i)
        ans = ans / (i+1)
    return ans
# Time Complexity: O(r)
# Space Complexity: O(1)        
#-------------------------------------------------------------
# Test: Print element at 5th row and 4th column. 
# Solution: So to print the element at the 5th row and 4th column we simply need to find (5-1)C(4-1) i.e. 4C3, so 
row = 5
col = 4
ans_element = nCr(row-1, col-1)
ans_element_from_optimized = optimized_nCr(row-1, col-1)
print(ans_element)
print(ans_element_from_optimized)
######################################################################################################################
# Problem Type 2: Given row number N, print all the elements in row Nth of the pascal triangle.
# Brute Force Approach: FInd all the elements of the Nth row of the Pascal triangle using the fomula nCr.
# Since we know that in Pascal triangle in Nth row we have N number of elements, so we can simply do as follows

def NthRowOfPascalTriangle(row):
    Nth_row = []
    for col in range(1, row+1):
        ele = nCr(row-1, col-1)
        Nth_row.append(ele)
    return Nth_row
# Time Complexity: O(n) . O(r) = O(n.r)
# Space Complexity: O(n) -> just to store the answer

#------------------Problem-2: Optimal Approach-----------------------------------------
# Optimal Approach: Use formula ele = (ele * (row-col)) / col, where col should be 0-indexed instead of 1-indexed
def NthRowOfPascalTriangle_Optimized(row):
    Nth_row = []
    ele = 1.0
    Nth_row.append(ele) # as 1st element will obviously be 1
    for col in range(1, row):
        ele = (ele * (row-col))/col
        Nth_row.append(ele)
    return Nth_row
# Time Complexity: O(n), where n is the number of elements in row n
# Space Complexity: O(n), just to store the answer
#------------Test Problem-2------------------
row = 5
print(NthRowOfPascalTriangle(row))
print(NthRowOfPascalTriangle_Optimized(row))

######################################################################################################################
# Problem Type 3: Given row Number N, print first N rows of the Pascal triangle

# Brute Force Approach: Find all the elements of the pascal triangle using nCr, but it's time complexity will be O(n^3)
# Optimized Approach: Iterate over each row and find the elements of each row using formula ele=(ele*(row-col))/col, where col is 0-indexed
def pascalTriangle(n):
    pascal_triangle=[]
    for row in range(1, n+1):
        row_elements=[]
        ele = 1.0
        row_elements.append(ele)
        for col in range(1, row):
            ele = (ele*(row-col))/col
            row_elements.append(ele)
        pascal_triangle.append(row_elements)
    return pascal_triangle
n = 5
print(pascalTriangle(n))

# Time Complexity: O(n) to iterate over n rows, and O(n) to find the all the elements of each row, so roughly
# the time complexity will be O(n^2)

