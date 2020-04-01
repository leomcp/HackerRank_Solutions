#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    am_pm = s[-2:]
    time = int(s[0:2])

    if am_pm == 'AM':
        if time == 12:
            s = '00'+s[2:-2]
        else:
            s = s[0:-2]

    elif am_pm == 'PM':
        if time == 12:
            s = s[0:-2]
        else:  
            time = time +12
            s = str(time)+s[2:-2]
    else:
        assert False 
    
    return s

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
