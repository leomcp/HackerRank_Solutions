#!/bin/python3

import os
import sys

#
# Complete the downToZero function below.
#
def downToZero(n):
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
