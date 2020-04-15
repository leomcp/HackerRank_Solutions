#!/bin/python3

import os
import sys

#
# Complete the treeCoordinates function below.
#
def treeCoordinates(n, edges, points):
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    edges = []

    for _ in range(n-1):
        edges.append(list(map(int, input().rstrip().split())))

    points = []

    for _ in range(m):
        points.append(list(map(int, input().rstrip().split())))

    result = treeCoordinates(n, edges, points)

    fptr.write(str(result) + '\n')

    fptr.close()
