#  Problem statement

# There is a frog on the '1st' step of an 'N' stairs long staircase. The frog wants to reach the 'Nth' stair. 'HEIGHT[i]' is the height of the '(i+1)th' stair.If Frog jumps from 'ith' to 'jth' stair, the energy lost in the jump is given by absolute value of ( HEIGHT[i-1] - HEIGHT[j-1] ). If the Frog is on 'ith' staircase, he can jump either to '(i+1)th' stair or to '(i+2)th' stair. Your task is to find the minimum total energy used by the frog to reach from '1st' stair to 'Nth' stair.
# For Example

# If the given ‘HEIGHT’ array is [10,20,30,10], the answer 20 as the frog can jump from 1st stair to 2nd stair (|20-10| = 10 energy lost) and then a jump from 2nd stair to last stair (|10-20| = 10 energy lost). So, the total energy lost is 20.

# Problem Link:- https://www.naukri.com/code360/problems/frog-jump_3621012?leftPanelTabValue=PROBLEM
# Solution Link:- https://www.geeksforgeeks.org/minimum-cost-for-hopping-frog-to-reach-stair-n/

from os import *
from sys import *
from collections import *
from math import *

from typing import *

"""
f(n) = min(f(n-1)+abs(H[n]-H[n-1]), f(n-2)+abs(H[n]-H[n-2]) ), i.e. f(n) = min(left, right) as per the following implementation
"""
def frog_energy(step: int, heights: List[int], memo: List[int])->int:
    if step == 0:
        return 0
    
    if memo[step]!=-1:
        return memo[step]

    # Left case: Frog bounces 1 floor, and energy is exhausted from the previous floor to the current floor
    left = frog_energy(step-1, heights,memo) + abs(heights[step] - heights[step-1] )
    right = float('inf')
    if step>1:
        right = frog_energy(step-2, heights, memo) + abs(heights[step]-heights[step-2])
    memo[step] = min(left, right)
    return memo[step]
def frogJump(n: int, heights: List[int]) -> int:
    memo = [-1]*(n+1)
    return frog_energy(n-1, heights,memo)

    