#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
# {1:2, 2:4, 3:3, 4:4}
def migratoryBirds(arr):
    frequentBird, frequency = 1, 0 
    birdsDict = {}
    for i in arr:
        if i not in birdsDict.keys():
            birdsDict[i] = 1
        else:
            birdsDict[i] = birdsDict[i] + 1
            
    for bird in birdsDict.keys():
        if birdsDict[bird] > frequency:
            frequency = birdsDict[bird]
            frequentBird = bird 
        if birdsDict[bird] == frequency:
            if bird < frequentBird:
                frequentBird = bird 

    
    return frequentBird


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
