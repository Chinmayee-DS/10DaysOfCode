# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
import sys
import math
import numpy as np
from statistics import mean

t = int(input())
for x in range(t):
    n = int(input())
    gpa = list(map(float, input().split()))
    #print(gpa)
    max_coef = -2
    for i in range(5):
        ys = list(map(float, input().split()))
        coef = np.corrcoef(gpa, ys)[0,1]
        #print(coef)
        if coef > max_coef:
            max_coef = coef
            max_i = i
    print(max_i+1)