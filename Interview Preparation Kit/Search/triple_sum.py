#!/bin/python

import math
import os
import random
import re
import sys

# Complete the triplets function below.
# Complete the triplets function below.
def _binarySearch(arr, key):
    if arr[0] > key:
        return 0
    elif arr[len(arr)-1] <= key:
        return len(arr)
    else:
        low = 0
        high = len(arr) -1 
        while(low<=high):
            mid = low + (high-low)/2
            if arr[mid] == key:
                return mid +1 
            elif arr[mid] < key and arr[mid +1] > key:
                return mid +1 
            elif arr[mid] > key and arr[mid -1] < key:
                return mid 
            elif arr[mid] > key:
                high = mid-1 
            elif arr[mid] < key:
                low = mid + 1

def triplets(a, b, c):
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    
    noOfTriplets = 0 
    for i in b:
        n_a, n_c = 0, 0
        n_a = _binarySearch(a, i) 
        n_c = _binarySearch(c, i)
        print(i, n_a, n_c)
        noOfTriplets = noOfTriplets + (n_a*n_c)
    return noOfTriplets

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    lenaLenbLenc = raw_input().split()
    lena = int(lenaLenbLenc[0])
    lenb = int(lenaLenbLenc[1])
    lenc = int(lenaLenbLenc[2])
    arra = map(int, raw_input().rstrip().split())
    arrb = map(int, raw_input().rstrip().split())
    arrc = map(int, raw_input().rstrip().split())
    ans = triplets(arra, arrb, arrc)
    fptr.write(str(ans) + '\n')
    fptr.close()
