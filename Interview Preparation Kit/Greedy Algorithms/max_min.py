import os
import sys
import re
import math
import random


def maxMin(k, arr):
	unfairness = sys.maxsize
	arr.sort()
	for i in range(len(arr)-k+1):
		
		unfairness = min(arr[i+k-1]-arr[i], unfairness)
		
	return unfairness
	
	
if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	n = int(input())
	k =  int(input())
	arr =[]
	for _ in range(n):
		arr_item = int(input())
		arr.append(arr_item)
	result = maxMin(k, arr)
	fptr.write(str(result) + '\n')
	fptr.close()
		
