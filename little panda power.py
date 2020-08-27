#!/bin/python

from __future__ import print_function

import os
import sys

# Complete the solve function below.
def solve(a, b, x):
    if b >= 0:
        p = a
    else:
        x0 = x
        x1 = x
        y = 0
        z = 1
        if(x1 == 1):
            return 0
        while(a > 1):
            quo = a / x1
            t = x1

            x1 = a % x1
            a = t
            t = y

            y = z - quo * y
            z = t
        if ( z < 0):
            z = z + x0
        p = z
    return pow(p, abs(b), x)     
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        abx = raw_input().split()

        a = int(abx[0])

        b = int(abx[1])

        x = int(abx[2])

        result = solve(a, b, x)

        fptr.write(str(result) + '\n')

    fptr.close()
