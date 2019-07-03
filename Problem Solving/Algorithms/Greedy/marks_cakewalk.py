import os 
import sys 
import math
import re

def quickSort(arr):
	if len(arr)<= 1:
		return arr
	left, equal, right = [],[],[]
	pivot = arr[0]
	for x in arr:
		if x< pivot:
			right.append(x)
		if x== pivot:
			equal.append(x)
		if x>pivot:
			left.append(x)
	arr= quickSort(left)+equal+quickSort(right)
	return arr

def marksCakewalk(calorie):
	miles=0
	sortedcalories = quickSort(calorie)
	for idx, val in enumerate(sortedcalories):
		miles = miles + (2**idx * val)
	return miles
		
if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	n = int(input())
	arr = list(map(int, input().rstrip().split()))
	
	res = marksCakewalk(arr)
	fptr.write(str(res)+'\n')
	fptr.close()
    
