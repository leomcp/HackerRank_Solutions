#!/bin/python3

import os
import sys

#
# Complete the andXorOr function below.
#
def andXorOr(a):
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = andXorOr(a)

    fptr.write(str(result) + '\n')

    fptr.close()
