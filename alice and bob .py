#!/bin/python

from __future__ import print_function

import os
import sys
import math

#
# Complete the sillyGame function below.
#
    #
    # Write your code here.
    #

def primelist():
    prime = []
    res = [True for i in range(100001)]
    for i in range(2, int(math.sqrt(100000))):
        a = i * i
        if res[i] == True:
            for j in range(a, 100001, i):
                res[j] = False
    for i in range(2, 100001):
        if res[i] == True:
            prime.append(i)
    return(prime)            

def sillyGame(n, p):
    ogl = list(range(1, n+1))
    num = len(list(set(p).intersection(ogl)))
    if num % 2 == 0:
        #print ("Bob")
        return "Bob"
    else:
        #print ("Alice")
        return "Alice"

   


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(raw_input())
    p =[]
    for g_itr in xrange(g):
        n = int(raw_input())

        if g_itr == 0:
            p = primelist()

        result = sillyGame(n, p)

        fptr.write(result + '\n')

    fptr.close()
