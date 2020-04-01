#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    idx = len(s) - 1
    while(idx >= 0):
        if s[idx] == s[idx-1]:
            s = s[0:idx-1:] + s[idx+1::]
            idx = len(s) -1 
        else:
            idx = idx - 1 
    if s == "":
        return "Empty String"
    else:
        return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
