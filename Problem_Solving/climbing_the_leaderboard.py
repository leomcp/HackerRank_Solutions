#!/bin/python

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def _getinitRank(arr):
    initRank = [0] * len(arr)
    initRank[0] = 1 
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            initRank[i] = initRank[i-1]
        else:
            initRank[i] = initRank[i-1] + 1
    return initRank

def _binarySearch(arr, key):
    low = 0
    high = len(arr) - 1

    while(low <= high):
        mid = low + (high - low)/2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key and arr[mid - 1] > key:
            return mid
        elif arr[mid] > key and arr[mid + 1] < key:
            return mid + 1
        elif arr[mid] > key:
            low = mid + 1
        elif arr[mid] < key:
            high = mid - 1
        

def climbingLeaderboard(scores, alice):
    initRank = _getinitRank(scores)
    result = [0] * len(alice)
    for idx, val in enumerate(alice):
        if val > scores[0]:
            result[idx] = 1
        elif val < scores[-1]:
            result[idx] = initRank[-1] + 1 
        else:
            index = _binarySearch(scores, val)
            result[idx] = initRank[index]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(raw_input())

    scores = map(int, raw_input().rstrip().split())

    alice_count = int(raw_input())

    alice = map(int, raw_input().rstrip().split())

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
