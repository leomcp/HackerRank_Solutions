import os
import sys
import re
import math
import random



def getMinimumCost(k, c):
	c.sort(reverse = True)
	minCost = 0
	prev = -1
	for idx, cost in enumerate(c):
		if idx%k == 0:
			prev+=1
		minCost = (prev + 1)*cost + minCost
	
	return minCost



if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	nk = input().split()
	n = int(nk[0])
	k = int(nk[1])
	
	c = list(map(int, input().rstrip().split()))
	minimumCost = getMinimumCost(k, c)
	fptr.write(str(minimumCost) + '\n')
	fptr.close()
		
