#!/bin/python3

import math
import os
import random
import re
import sys
import datetime
from datetime import datetime 

# Complete the time_delta function below.
def time_delta(t1, t2):
    # format = Day dd Mon yyyy hh:mm:ss +xxxx
    format = '%a %d %b %Y %H:%M:%S %z'
    time_diff = int(abs((datetime.strptime(t1, format)-datetime.strptime(t2, format)).total_seconds()))
    return str(time_diff)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
