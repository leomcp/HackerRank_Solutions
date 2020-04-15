#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(arr):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
