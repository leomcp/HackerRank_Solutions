#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(tree, queries):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    tree = []

    for _ in range(n-1):
        tree.append(list(map(int, input().rstrip().split())))

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(tree, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
