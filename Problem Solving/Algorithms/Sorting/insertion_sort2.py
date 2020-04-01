import os
import sys
import math
import random

def _swapElem(arr, idx1, idx2):
	arr[idx1]= arr[idx1]+arr[idx2]
	arr[idx2] = arr[idx1]-arr[idx2]
	arr[idx1]= arr[idx1]-arr[idx2]

def insertionSort2(arr):
	i=1
	while(i< len(arr)):	
		k,j=i,i-1
		while(j>=0 and k>=0):
			if arr[k]<arr[j]:
				_swapElem(arr, k, j)
			j=j-1
			k =k-1
		print(*arr, sep=" ")
		i=i+1
		
		
#arr =[1,4,3,5,6,2]
#insertionSort2(arr)

if __name__ == "__main__":
	n=int(input())
	arr = list(map(int, input().rstrip().split()))
	insertionSort2(arr)