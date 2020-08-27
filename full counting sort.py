#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):  
    for i in range(n):
        arr1 = arr[i]
        arr1.append(i)
    #arr.sort(key = lambda x:x[0])
    for x in range(n):
        arr[x][0] = int(arr[x][0])
    arr.sort(key = lambda x:x[0])
    for i in range(n):
        if arr[i][2] < (n/2):
            arr[i][1] = '-'
    for x in range(n):
        print(arr[x][1]),
    

if __name__ == '__main__':
    n = int(raw_input().strip())

    arr = []

    for x in range(n):
        arr.append(raw_input().rstrip().split())
    countSort(arr)