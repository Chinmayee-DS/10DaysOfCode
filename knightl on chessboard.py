#!/bin/python

import math
import os
import random
import re
import sys

# Complete the knightlOnAChessboard function below.
def Br_Ft_Sch(n,i,j):
    queue = set()
    queue.add((0,0))
    dest = (n-1,n-1)
    stack = [(0,0)]
    if i != j:
        step = [(i,j),(i,-j),(-i,j),(-i,-j),(j,i),(j,-i),(-j,i),(-j,-i)]
    else:
        step = [(i,i),(i,-i),(-i,i),(-i,-i)]
    count = 0
    while stack:
        count = count + 1
        m = len(stack)
        while m > 0:
            m = m - 1
            x, y = stack.pop(0)
            for stepx, stepy in step:
                x1, y1 = x + stepx, y + stepy
                if (x1,y1) == dest:
                    return count
                if 0 <= x1 < n and 0 <= y1 < n and (x1,y1) not in queue:
                    queue.add((x1,y1))
                    stack.append((x1,y1))
    return -1
            
def knightlOnAChessboard(n):
    ans = [[0]*(n-1) for x in range(n-1)]
    for i in range(n-1):
        for j in range(i,n-1):
            ans[i][j] = Br_Ft_Sch(n,i+1,j+1)
    for i in range(n-1):
        for j in range(i+1,n-1):
            ans[j][i] = ans[i][j]
    return ans
            
#ans=knightlOnAChessboard(5)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
