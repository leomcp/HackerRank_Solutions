#!/bin/python3

import os
import sys

#
# Complete the jennysSubtrees function below.
#
def jennysSubtrees(n, r, edges):
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().split()

    n = int(nr[0])

    r = int(nr[1])

    edges = []

    for _ in range(n-1):
        edges.append(list(map(int, input().rstrip().split())))

    result = jennysSubtrees(n, r, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
