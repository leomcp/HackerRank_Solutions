#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    start  = 1
    end = len(arr) - 1
    maxSum = -1000
    
    for row in range(start, end):
        for col in range(start, end):
            first =arr[row-1][col-1] + arr[row-1][col] + arr[row-1][col+1]
            middle = arr[row][col]
            last = arr[row+1][col-1] + arr[row+1][col] + arr[row+1][col+1]
            total =  first + middle + last 

            if total > maxSum:
                maxSum = total
                

    
    return maxSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
