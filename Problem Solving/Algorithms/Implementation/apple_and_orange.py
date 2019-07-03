#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def checkPos(s, t, a_or_b, fruit):
    n = 0 
    for i in fruit:
        check = a_or_b + i
        if check >= s and check <= t:
            n += 1 
    print(n)
    

def countApplesAndOranges(s, t, a, b, apples, oranges):
    checkPos(s, t, a, apples)
    checkPos(s, t, b, oranges)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
