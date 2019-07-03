import os
import sys
import re
import random
import math


def bigSorting(unsorted):
	unsorted.sort(key = lambda x : (len(x), x))

if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	q = int(input())
	unsorted = []
	
	for _ in range(q):
		unsorted_item = input()
		unsorted.append(unsorted_item)
		
	bigSorting(unsorted)
	
	for i in unsorted:
		
		fptr.write(str(i)+'\n')
		#fptr.write('\n')
	fptr.close()
    
    