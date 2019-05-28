#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def calFeb(year):
    feb = 28
    offset = 0 
    if year == 1918:
        offset = 13 
    if year < 1918:
        if (year % 4) == 0:
            feb = 29
    elif ((year % 400) == 0) or ((year%4 == 0) and (year%100 != 0)):
        feb = 29
    feb = feb - offset 
    return feb


def dayOfProgrammer(year):

    noDayMon = 215 + calFeb(year)
    day = 256 - noDayMon
    date = str(day)+".09."+str(year)
    return date 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
