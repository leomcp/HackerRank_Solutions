#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def getSum(arr):
    total = 0 
    for i in arr:
        total += i
    print("Total:", total)
    return total 

def miniMaxSum(arr, total):
    min = total
    max = 0

    for i in arr:
        a = total - i

        if min > a:
            min = a 
        if max < a:
            max = a
    
    return min, max 


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    total = getSum(arr)

    min, max = miniMaxSum(arr, total)
    print(min, max)
