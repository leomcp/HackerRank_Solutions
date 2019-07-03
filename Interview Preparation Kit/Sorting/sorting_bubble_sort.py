#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def swap(arr, idx1, idx2):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp 

def countSwaps(arr):
    no_of_swaps = 0
    do_sorting = True 
    n = len(arr) - 1
    last_sorted = n

    while(do_sorting):
        do_sorting = False
        for i in range(0, last_sorted):
            if arr[i] > arr[i+1]:
                do_sorting = True
                swap(arr, i, i+1)
                no_of_swaps += 1

    return no_of_swaps, arr[0], arr[n] 


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    no_of_swaps, first_elem, last_elem = countSwaps(a)
    print("Array is sorted in",no_of_swaps,"swaps.")
    print("First Element:",first_elem)
    print("Last Element:",last_elem)
