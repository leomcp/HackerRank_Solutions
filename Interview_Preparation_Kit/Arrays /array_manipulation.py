#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * n 
    maxNum = -1000

    for idx, val in enumerate(queries):
        start, end, numtoAdd = val[0], val[1], val[2]
        arr[start - 1] = arr[start - 1] + numtoAdd
        if (end < n):
            arr[end] = arr[end] - numtoAdd
    
    for i in range(1, len(arr)):  
        arr[i] = arr[i-1] + arr[i]
        if arr[i] > maxNum:
            maxNum = arr[i]
    
    return maxNum
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
