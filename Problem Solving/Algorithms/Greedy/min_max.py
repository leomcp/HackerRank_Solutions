#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    unfairness = sys.maxsize
    arr.sort()
    
    for idx in range(len(arr)-k+1):
        print(idx, arr[idx], arr[idx+k-1])
        unfairness = min(unfairness, arr[idx+k-1]-arr[idx])
        
    return unfairness 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
