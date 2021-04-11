#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    
    hashTable = {}
    
    for item in arr:
        if item in hashTable:
            hashTable[item] = hashTable[item] + 1
        else:
            hashTable[item] = 1

    maxElem = 0
    for item in hashTable:
        maxElem = max(maxElem, hashTable[item])
 
    return len(arr) - maxElem
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
