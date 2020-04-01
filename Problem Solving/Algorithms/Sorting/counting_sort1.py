import os
import re
import random
import math
import sys


def countingSort(arr):
	
	countsorted = [0]*100
	for i in arr:
		countsorted[i] = countsorted[i] + 1
	return countsorted


if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	n = int(input())
	
	arr = list(map(int, input().rstrip().split()))
	
	res = countingSort(arr)
	fptr.write(' '.join(map(str, res)))
	fptr.write('\n')
	fptr.close()
    
    
    