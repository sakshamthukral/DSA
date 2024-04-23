# def findSPecialSubstrings(s:str):
#     special_substring_matrix = []
#     i=0
#     while i<len(s):
#         current_char = s[i]
#         length = 1
#         while i + length<len(s) and s[i+length] == current_char:
#             length+=1
#         substring = s[i:i+length]

#         # check if the substring is already in the matrix
#         found = False
#         for row in special_substring_matrix:
#             if row[0] == substring:
                
