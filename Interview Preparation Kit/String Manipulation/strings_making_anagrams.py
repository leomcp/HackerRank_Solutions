import os
import math
import re
import sys
import random

def getDict(s1, s2):
	strdict = {}
	for i in s1:
		if i in strdict.keys():
			strdict[i][0] += 1
			strdict[i][1] = 0
		else: 
			strdict.setdefault(i, []).append(1)
			strdict.setdefault(i, []).append(0)
		
	for i in s2:
		if i in strdict.keys():
			strdict[i][1] += 1
		else:
			strdict.setdefault(i, []).append(0)
			strdict.setdefault(i, []).append(1)
			
	return strdict
	
def makeAnagram(a,b):
	countDel = 0
	strdict ={}

	strdict = getDict(a,b)
	
	for key, arr in strdict.items():
		diff = abs(arr[0]-arr[1])
		countDel = countDel + diff
	
	return countDel

if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	a = input()
	b = input()
	res = makeAnagram(a, b)
	fptr.write(str(res)+'\n')
	fptr.close()
    
    