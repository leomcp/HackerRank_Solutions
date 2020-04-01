import os
import sys
import re
import random
import math


def countSort(arr):
	countDict ={}
	output = []
	for idx, val in enumerate(arr):
		key = val[0]
		if idx < len(arr)//2:
			x = '-'
		else: x = val[1]
		
		if key in countDict.keys():
			countDict[key].append(x)
		else:
			countDict.setdefault(key, []).append(x)
			
	for i in sorted(countDict.keys()):
		for j in countDict[i]:
			output.append(j)
	
	return output

	

#countSort([(0,'a'), (1,'b'),(0,'c'),(1,'d'), (1,'e')])
    
if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	q = int(input().strip())
	arr=[]
	
	for _ in range(q):
		arr.append(input().rstrip().split())
		
	res = countSort(arr)
	fptr.write(" ".join(map(str, res)))
	fptr.close()
    
    
    