import os
import re
import random
import math


def closestNumbers(arr):
	resarr =[]
	arr.sort()
	mindiff = arr[1]-arr[0]
	
	for i in range(1, len(arr)):
		diff = arr[i]-arr[i-1]
		if diff<mindiff:
			resarr = []
			resarr.append(arr[i-1])
			resarr.append(arr[i])
			mindiff = diff
		elif diff == mindiff:
			resarr.append(arr[i-1])
			resarr.append(arr[i])
	return resarr

if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	n = int(input())
	
	arr = list(map(int, input().rstrip().split()))
	
	res = closestNumbers(arr)
	fptr.write(' '.join(map(str, res)))
	fptr.write('\n')
	fptr.close()
    
    