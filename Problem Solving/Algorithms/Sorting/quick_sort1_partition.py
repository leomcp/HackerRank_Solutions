import os
import random
import sys
import math
import re


def quickSort(arr):
	pivot = arr[0]
	left, equal, right = [], [], []
	
	for i in arr:
		if i > pivot: 
			right.append(i)
		if i== pivot:
			equal.append(i)
		if i < pivot:
			left.append(i)
		
	return left+equal+right
	


print(quickSort([4,5,3,7,2]))
    

if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	n = int(input())
	
	arr = list(map(int, input().rstrip().split()))
	
	res = quickSort(arr)
	fptr.write(' '.join(map(str, res)))
	fptr.write('\n')
	fptr.close()
    
    
