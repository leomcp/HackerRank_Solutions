#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    end = len(c) - 1
    i = 0 
    jumps = 0 

    while(i < end):
        if((i + 2 ) <= end) and (c[i + 2] == 0):
            jumps += 1
            i += 2
        elif (c[i + 1] == 0):
            jumps += 1
            i += 1 

    return jumps 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
