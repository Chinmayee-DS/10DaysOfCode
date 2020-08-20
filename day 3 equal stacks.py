#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.

    a = sum(h1)
    b = sum(h2)
    c = sum(h3)
    while(a != b or b != c or c != a):
        big = a
        if b > big:
            big = b
        if c > big:
            big = c           
        
        if big == a:
            a = a - h1[0]
            h1.pop(0)
        elif big == b:
            b = b - h2[0]
            h2.pop(0)
        else :
            c = c - h3[0]
            h3.pop(0)
       
        
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = raw_input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = map(int, raw_input().rstrip().split())

    h2 = map(int, raw_input().rstrip().split())

    h3 = map(int, raw_input().rstrip().split())

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
