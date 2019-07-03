import os
import sys
import random
import math


def alternateCharacters(a):
	delChar = 0
	for i in range(len(a)-1):
		if a[i] == a[i+1]:
			delChar+=1
	return delChar



if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	q = int(input())
	
	for q_itr in range(q):
		s = input()
		res = alternateCharacters(s)
		fptr.write(str(res)+'\n')
	fptr.close()
    
