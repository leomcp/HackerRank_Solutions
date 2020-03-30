#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def pickingNumbers(a):
    a.sort()
    maxCount, j = 0, 1

    for idx in range(0, len(a), j):
        arr = [a[idx],]

        for idx2 in range(idx + 1, len(a), 1):
            if abs(a[idx] - a[idx2]) <= 1:
                arr.append(a[idx2])
            else:
                break
        j = idx2 + idx 

        if maxCount < len(arr):
            maxCount = len(arr)

    return maxCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
