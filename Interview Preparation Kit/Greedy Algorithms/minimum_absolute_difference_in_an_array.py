
import math
import os
import random
import re
import sys


def minimumAbsoluteDifference(arr):
	arr.sort()
	minDiff = arr[-1]-arr[0]
	for i in range(0, len(arr)-1):
		diff = arr[i+1]-arr[i]
		if minDiff >= diff:
			minDiff = diff
	return minDiff



if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	n = int(input())
	arr = list(map(int, input().rstrip().split()))
	result = minimumAbsoluteDifference(arr)
	fptr.write(str(result)+'\n')
	fptr.close()


#arr = [1, -3, 71, 68, 17]

#print(minimumAbsoluteDifference(arr))
