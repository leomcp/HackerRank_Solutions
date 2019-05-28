#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def _getSum(arr):
    sumarr = 0 
    for i in arr:
        sumarr = sumarr + i
    return sumarr

def balancedSums(arr):
    x = 0 
    arr_sum = _getSum(arr)
    for y in arr: 
        if (2 * x) == (arr_sum - y):
            return "YES"
        else:
            x = x + y
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
