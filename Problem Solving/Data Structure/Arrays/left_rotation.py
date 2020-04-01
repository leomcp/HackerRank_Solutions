#!/bin/python3

import math
import os
import random
import re
import sys

def leftRotate(arr, d):
    newlist = arr[d%len(arr):] + arr[:d%len(arr)]
    return newlist

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = leftRotate(a, d)

    for i in result:
        print(i, end=" ")
