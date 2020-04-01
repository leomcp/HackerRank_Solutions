#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def _swapArr(arr, idx1, idx2):
    arr[idx1] = arr[idx1] + arr[idx2]
    arr[idx2] = arr[idx1] - arr[idx2]
    arr[idx1] = arr[idx1] - arr[idx2]

def minimumSwaps(arr):
    minSwaps, idx = 0, 0
    while(idx <= (len(arr)-1)):
        if arr[idx] == (idx+1):
            idx += 1
        else:
            _swapArr(arr, idx, (arr[idx]-1))
            minSwaps += 1
    return minSwaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
