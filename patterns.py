from typing import List

# Pattern-1
# *****
# ****
# ***
# **
# *
def pattern1(n: int):
    for i in range(n):
        for j in range(n-i):
            print("*", end=" ")
        print()


# Pattern-2
# 12345
# 1234
# 123
# 12
# 1
def pattern2(n: int):
    for i in range(n):
        for j in range(1,n-i+1):
            print(j, end=" ")
        print()


# Pattern-3
#     *    
#    ***   
#   *****  
#  ******* 
# *********
def pattern3(n: int)-> None:
    for i in range(n):
        # inner loop for spaces
        for j in range(n-i-1):
            print(" ",end="")
        # inner loop for stars
        for j in range((2*i)+1):
            print("*", end=" ")
        # inner loop for spaces
        for j in range(n-i-1):
            print(" ",end="")
        print()


# Pattern-4
# *********
#  *******
#   *****
#    ***
#     *
def pattern4(n: int)-> None:
    for i in range(n-1,-1,-1):
        # inner loop for spaces
        for j in range(n-i-1):
            print(" ",end="")
        # inner loop for stars
        for j in range((2*i)+1):
            print("*", end=" ")
        # inner loop for spaces
        for j in range(n-i-1):
            print(" ",end="")
        print()

# Pattern-5
#   *
#  ***
# *****
# *****
#  ***
#   *
def pattern5(n: int)->None:
    for i in range(n):
        # inner loop for spaces
        for j in range(n-i-1):
            print(" ",end="")
        # inner loop for stars
        for j in range((2*i)+1):
            print("*", end="")
        # inner loop for spaces
        for j in range(n-i-1):
            print(" ",end="")
        print()
    for i in range(n-1,-1,-1):
        # inner loop for spaces
        for j in range(n-i-1):
            print(" ",end="")
        # inner loop for stars
        for j in range((2*i)+1):
            print("*", end="")
        # inner loop for spaces
        for j in range(n-i-1):
            print(" ",end="")
        print()

# Pattern-6
# Input Format: N = 6
# Result:   
#      *
#      **
#      *** 
#      ****
#      *****
#      ******  
#      *****
#      ****
#      ***    
#      **
#      *
def pattern6(n:int)->None:
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()
    new_n = n-1
    for i in range(new_n):
        for j in range(new_n-i):
            print("*", end="")
        print()

# Pattern-7
# N=3
# 1
# 0 1
# 1 0 1
def pattern7(n:int)->None:
    start = 1
    for i in range(n):
        if i%2 == 0:
            start = 1
        else:
            start = 0
        for j in range(i+1):
            print(start,end="")
            start = 1-start
        print()


# Pattern-12
# Example:
# Input: ‘N’ = 3

# Output: 

# 1         1
# 1 2     2 1
# 1 2 3 3 2 1

def pattern12(n:int)->None:
    spaces = 2*(n-1)
    for i in range(1,n+1):
        # Number
        for j in range(i):
            print(j+1,end=" ")
        # Spaces
        for j in range(spaces):
            print(" ",end=" ")
        # Number
        for j in range(i,0,-1):
            print(j, end=" ")
        print()
        spaces-=2

# Pattern 14
# A
# A B
# A B C
def pattern14(n:int)->None:
    for i in range(n):
        for j in range(i+1):
            print(chr(ord('A')+j),end= "")
        print()

# Pattern 17
# Example:
# Input: ‘N’ = 3

# Output: 
#     A
#   A B A
# A B C B A
def pattern17(n:int)->None:
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end =" ")
        for j in range(i+1):
            print(chr(ord('A')+j),end= " ")
        for j in range(i, 0, -1):
            print(chr(ord('A')+j-1),end= " ")
        for j in range(n-i-1):
            print(" ", end=" ")
        print()
    
# Pattern-18
# Input Format: N = 3
# Result: 
# C
# B C
# A B C

# Input Format: N = 6
# Result:   
# F
# E F
# D E F
# C D E F
# B C D E F
# A B C D E F

def pattern18(n:int)->None:
    for i in range(n): 
        character = ord('A')+n-1
        for j in range(character-i, character+1): 
            print(chr(j),end=" ")
        print()

def pattern19(n:int)->None:
    for i in range(n): 
        character = ord('A')+n-1 # Play on the order/ASCII value of character in case of patterns printing for characters
        for j in range(character,character-i-1, -1): 
            print(chr(j),end=" ")
        print()


# Pattern 20
# * * * * * * 
# * *     * * 
# *         * 
# *         * 
# * *     * * 
# * * * * * *

def pattern20(n:int)->None:
    for i in range(n): 
        for j in range(n-i):
           print("*",end=" ")
        for j in range(2*i):
           print(" ",end=" ")
        for j in range(n-i):
              print("*",end=" ")
        print()
    for i in range(n): 
        for j in range(i+1):
           print("*",end=" ")
        for j in range(2*(n-1-i)):
           print(" ",end=" ")
        for j in range(i+1):
              print("*",end=" ")
        print()


# Pattenr 21
# Example:
# Input: ‘N’ = 3

# Output: 
# *         *
# * *     * *
# * * * * * *
# * *     * *
# *         *
def pattern21(n:int)->None:
    for i in range(n): 
        for j in range(i+1):
           print("*",end=" ")
        for j in range(2*(n-i-1)):
           print(" ",end=" ")
        for j in range(i+1):
              print("*",end=" ")
        print()
    new_n = n-1
    for i in range(new_n): 
        for j in range(new_n-i):
           print("*",end=" ")
        for j in range(2*(i+1)):
           print(" ",end=" ")
        for j in range(new_n-i):
              print("*",end=" ")
        print()
        
# Pattern 22
# Example:
# Input: ‘N’ = 4

# Output: 

# ****
# *  *
# *  *
# ****

def pattern22(n:int)->None:
    for i in range(n):
        if i == 0 or i == n-1:
            for j in range(n):
                print("*",end=" ")
        else:
            for j in range(n):
                if j == 0 or j == n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
        print()

# Pattern-23
# Example:
# Input: ‘N’ = 4

# Output: 

# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444

def pattern23(n:int)->None:
    for i in range(2*n-1):
        for j in range(2*n-1):
            top_distance = i
            left_distance = j
            right_distance = (2*n-1)-1-j # 2*n-1 is the total number of columns so 2*n-1-1 is the last index and j is the current index
            bottom_distance = (2*n-1)-1-i # 2*n-1 is the total number of rows so 2*n-1-1 is the last index and i is the current index
            min_distance = min(top_distance, left_distance, right_distance, bottom_distance)
            print(n-min_distance,end=" ")
        print()



# pattern1(5)
# pattern2(5)
# pattern3(5)
# pattern4(5)
# print("----------")
# pattern5(3)
# pattern6(6)
# pattern7(3)
# pattern12(3)
# pattern14(3)
# pattern16(3)
# pattern18(6)
# pattern19(3)
# pattern20(5)
# pattern21(3)
# pattern22(4)
pattern23(4)