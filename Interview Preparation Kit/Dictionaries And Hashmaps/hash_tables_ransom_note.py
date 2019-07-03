#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mag = Counter(magazine)
    no = Counter(note)
    
    flag = 'Yes'
    
    for word in note:
        if mag[word] > 0:
            mag[word] -= 1
        else:
            flag = 'No'
            break 
            
    print(flag)

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
