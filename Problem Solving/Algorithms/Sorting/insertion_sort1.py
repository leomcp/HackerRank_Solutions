import math
import os 
import sys
import random
import re
	
def insertionSort1(n, arr):
	i= n-2
	checkNo = arr[-1]
	
	while(i>=0):
		if checkNo < arr[i]:
			arr[i+1] = arr[i]
			print(*arr, sep=" ")
			if i==0:
				arr[0] = checkNo
				print(*arr, sep= " ")
				break
			i-=1
		else:
			arr[i+1] = checkNo
			print(*arr, sep = " ")
			break

if __name__ == "__main__":
	
	n = int(input())

	arr = list(map(int, input().rstrip().split()))
	insertionSort1(n, arr)
	
    
#insertionSort1(10, [2,3,4,5,6,7,8,9,10,1])