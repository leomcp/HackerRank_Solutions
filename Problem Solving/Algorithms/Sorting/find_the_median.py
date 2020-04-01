import os
import sys
import random
import re 

def findMedian(arr):
	arr.sort()
	n = len(arr)
	#print(n, arr)

	if (n%2) ==0:
		return (arr[n//2]+arr[n//2-1])//2
	else:
		return arr[n//2]


#arr =[0, 1,2,4,3,5]

#print(findMedian(arr))


if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	n = int(input())
	
	arr = list(map(int, input().rstrip().split()))
	res = findMedian(arr)
	fptr.write(str(res)+'\n')
	fptr.close()
    
