!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

while d > 0:
    b = a[0]
    a.pop(0)
    a.append(b)
    d = d - 1
for x in range(len(a)):
    print(a[x]),
    x =x + 1
