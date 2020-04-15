#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants(p):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
