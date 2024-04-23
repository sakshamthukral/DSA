from typing import List
# Return list of lists containing first n rows of the pascal triangle
# def generateRows(row:int)->List[int]:
#     ans = 1
#     pascalRow =[]
#     pascalRow.append(ans)
#     for col in range(1,row):
#         ans = ans*(row-col)
#         ans = ans//col
#         pascalRow.append(ans)
#     return pascalRow

# def generatePascalTriangle(rows:int)->List[List[int]]:
#     pascalTriangle = []
#     for row in range(1,rows+1):
#         pascalTriangle.append(generateRows(row))
#     return pascalTriangle

def get_pascal_row(row:int)->List[int]:
    ans = 1
    pascalRow = []
    pascalRow.append(ans)
    for col in range(1, row):
        ans = ans*(row-col)
        ans = ans//col
        pascalRow.append(ans)
    return pascalRow
def get_pascal_triangle(rows:int) -> List[List[int]]:
    pascalTriangle = []
    for row in range(1, rows+1):
        pascalTriangle.append(get_pascal_row(row))
    return pascalTriangle



rows = 5
pascalTriangle = get_pascal_triangle(rows)
print(pascalTriangle)
