#!/bin/python3

import math
import os
import random
import re
import sys


def maximumToys(prices, k):
    no_of_toys = 0 
    prices.sort()

    for i in range(0, len(prices) - 1):
        k = k - prices[i]
        if k >= 0:
            no_of_toys += 1

    return no_of_toys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
