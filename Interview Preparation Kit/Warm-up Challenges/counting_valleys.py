#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    prev, curr, mountain, valley = 0, 0, 0, 0

    for i in range(n):
        prev = curr
        if s[i] == 'U':
            curr += 1 
        else:
            curr -= 1 

        if curr == 0:
            if prev > curr:
                mountain += 1 
            else:
                valley += 1 

    return valley
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
