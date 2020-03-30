#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
# [12, 24, 10, 24]
def breakingRecords(scores):
    min_max = [0]*2
    highest, lowest = scores[0], scores[0] 

    for score in scores:
        if score > highest:
            highest = score
            min_max[0] = min_max[0] + 1
        elif score < lowest:
            lowest = score 
            min_max[1] = min_max[1] + 1
    return min_max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
