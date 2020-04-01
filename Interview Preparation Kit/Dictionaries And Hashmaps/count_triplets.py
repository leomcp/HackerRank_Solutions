import math
import os
import random
import re
import sys

def getRank(arr):
	rank = {}
	for i in arr:
		if i in rank.keys():
			rank[i] = rank[i] + 1
		else:
			rank[i] = 1
	return rank

def countTriplets(arr, r):
	
	sum_array=[]
	if r==1:
		for i in range(len(arr)-1):
			sum_array.append((i*(i+1))/2)
		return sum(sum_array)
	count= 0
	rank = getRank(arr)
	startelemmap = {}
	for i in range(0, len(arr)-2):
		first = arr[i]
		second = first*r
		third = second*r
		noofset = 0
		if first not in startelemmap.keys():
			if second in rank.keys():
				if third in rank.keys():
					noofset = rank[first]*rank[second]*rank[third]
					startelemmap[first]=1
					print(first, second,third,noofset)
		count = count + noofset
	return count
		
		
	

if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	nr = input().rstrip().split()
	n = int(nr[0])
	r = int(nr[1])
	arr = list(map(int, input().rstrip().split()))
	result = countTriplets(arr,r)
	fptr.write(str(result)+'\n')
	fptr.close()


