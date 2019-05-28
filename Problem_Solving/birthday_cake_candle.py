#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    candledict = {}
    max = 0 

    for i in ar:
        if i in candledict:
            candledict[i] = candledict[i] + 1
        else:
            candledict[i] = 1 
        if i > max:
            max = i 

    return candledict.get(max)        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
