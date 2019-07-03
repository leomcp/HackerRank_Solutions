import math
import os
import re
import sys

def compareTriplets(a, b):

	res = [0,0]
	for i in range(3):
		if a[i]>b[i]:
			res[0] = res[0]+1
		elif a[i]<b[i]:
			res[1] = res[1]+1
	return res
		
#res = compareTriplets([5,6,7],[3,6,10])
#print(res)


if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	a = list(map(int, input().rstrip().split()))
	b = list(map(int, input().rstrip().split()))
	res = compareTriplets(a,b)
	fptr.write(' '.join(map(str,res)))
	fptr.write('\n')
	fptr.close()

