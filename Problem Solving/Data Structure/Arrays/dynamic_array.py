#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    result = []
    lastAnswer = 0
    listoflist = []
    for nitr in range(n):
        list = []
        listoflist.append(list)

    for arr in queries:
        seq = ((arr[1]^lastAnswer)%n)
        #print(seq)
        if arr[0] == 1:
            seqlist = listoflist[seq]
            seqlist.append(arr[2])
            #print(listoflist, 0)
        else:
            seqlist = listoflist[seq]
            #print(listoflist, 1)
            #print(seqlist, lastAnswer)
            lastAnswer = seqlist[arr[2]%len(seqlist)]
            result.append(lastAnswer)
    return result

#queries = [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]

#print(":", dynamicArray(2, queries))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
