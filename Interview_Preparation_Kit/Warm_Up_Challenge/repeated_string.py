#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    # counting no of a in s 
    aCount = 0 
    for i in s:
        if i == 'a':
            aCount +=1 

    str_len = len(s)
    ratio = n // str_len
    first = (n % str_len)
    remainder = str_len - first

    noOfa = ratio * aCount
    end = str_len - remainder

    for i in range(0, str_len - remainder):
        print(s[i])
        if s[i] == 'a':
            noOfa += 1

    #print(ratio, remainder, first, end , s[end])

    return noOfa


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
