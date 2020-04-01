#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    adict = {}

    for idx, val in enumerate(h):
        adict[alpha[idx]] = val
    
    maxHeight = 0
    for char in word:
        if maxHeight < adict[char]:
            maxHeight = adict[char]
    
    return maxHeight * len(word)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
