#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    for idx, val in enumerate(arr):
        for i in range(idx+1, len(arr)):
            if arr[i] == (m-val):
                return idx+1, i+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        m = int(input())
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        result = icecreamParlor(m, arr)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
    fptr.close()
