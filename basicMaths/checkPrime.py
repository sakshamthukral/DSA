from math import *
from collections import *
from sys import *
from os import *

def checkPrime(n):
    flag = "YES"
    if n  == 1:
        print("NO")
        return
    for i in range(2,int(sqrt(n))+1):
        if(n%i == 0):
            flag = "NO"
            break 
    print(flag)


n = int(input())
checkPrime(n)