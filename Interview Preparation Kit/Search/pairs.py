import os
import sys
import re
import random
import math

def quickSort(arr):
	if len(arr) == 0:
		return arr
	left, equal, right = [], [], []
	pivot = arr[0]
	for i in arr:
		if i > pivot : right.append(i)
		if i== pivot : equal.append(i)
		if i < pivot : left.append(i)
	arr = quickSort(left) + equal + quickSort(right)
	return arr 

def binarySearch(key, arr):
	print(arr,key)
	if len(arr)==0:
		return False
	if len(arr)==1:
		if arr[0]==key:
			return True
		else:
			return False
	mid = len(arr)//2
	if arr[mid]==key:
		return True
	else:
		if arr[mid]<key:
			return binarySearch(key, arr[mid:])
		else:
			return binarySearch(key, arr[:mid])

def pairsbinarySearch(k, arr):
	noofpairs=0
	sortedArr = quickSort(arr)
	print(sortedArr)
	if k == 1:	
		for i in range(len(sortedArr)-1):
			diff = sortedArr[i+1]-sortedArr[i]
			if diff ==k:
				noofpairs = noofpairs + 1
	else:
		for idx, val in enumerate(sortedArr):
			if val>k: 
				diff = val-k
				if binarySearch(diff, sortedArr[:idx]):
					noofpairs=noofpairs +1
	return noofpairs
	
def pairs(key, arr):
	arr.sort()
	i, j, pairs =0,1,0
	while(j<=len(arr)-1):
		diff = arr[j] -arr[i]
		if diff == key:
			pairs = pairs +1
			j=j+1
		else: 
			if diff<key:
				j=j+1
			else:
				i=i+1
	return pairs
	
if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	nk = input().split()
	n = int(nk[0])
	k = int(nk[1])
	
	arr = list(map(int, input().rstrip().split()))
	result = pairs(k, arr)
	fptr.write(str(result) + '\n')
	fptr.close()
		


    
    
    
    
    