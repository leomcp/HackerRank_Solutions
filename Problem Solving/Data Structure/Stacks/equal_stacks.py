#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def get_sum(arr):
    sumarr =0 
    for i in arr:
        sumarr = sumarr + i
    return sumarr


def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    s1, s2, s3 = get_sum(h1), get_sum(h2), get_sum(h3)
    print(h1, s1)
    print(h2, s2)
    print(h3, s3)
    
    while s1!=0 and s2!=0 and s3!=0 and (s1!=s2 or s2!=s3):
        print(s1, s2, s3)
        if max(s1, s2, s3) == s1:
            s1 = s1 - h1[0]
            h1.pop(0)
        elif max(s1, s2, s3) == s2:
            s2 = s2 - h2[0]
            h2.pop(0)
        elif max(s1, s2, s3) == s3:
            s3 = s3 - h3[0]
            h3.pop(0)
        
    if s1==s2 and s2==s3:
        return s1
    else:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
