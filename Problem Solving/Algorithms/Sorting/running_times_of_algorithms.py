import os
import math
import random
import sys

def _swapElem(arr, idx1, idx2):
	arr[idx1]=arr[idx1]+arr[idx2]
	arr[idx2]=arr[idx1]-arr[idx2]
	arr[idx1]=arr[idx1]-arr[idx2]
	
def insertionSort(arr):
	shifts = 0
	i=1
	while(i< len(arr)):
		j=i
		k=i-1
		while(j>=0 and k>=0):
			if(arr[j]<arr[k]):
				_swapElem(arr, j,k)
				shifts = shifts + 1
			j=j-1
			k=k-1
		i=i+1
		
	return shifts

def runningTime(arr):
	return insertionSort(arr)

	
#arr=[2,1,3,1,2]
#print(runningTime(arr))



if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	n = int(input())
	
	arr = list(map(int, input().rstrip().split()))
	
	res = runningTime(arr)
		
	fptr.write(str(res)+'\n')
	fptr.close()
    

    
    