#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    sticks.sort()
    n = len(sticks)
    idx = n-3
    while idx>=0 and (sticks[idx]+sticks[idx+1])<=sticks[idx+2]:
        idx = idx - 1
    
    if idx >=0:
        return [sticks[idx], sticks[idx+1], sticks[idx+2]]
    else:
        return [-1] 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
