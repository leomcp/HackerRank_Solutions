import os
import re
import math
import random

def substrCount(n, s):
	substrCount = 0
	sameChar = [0]*n
	
	i=0
	while(i<n):
		j = i+1
		sameCount = 0
		while(j<n):
			if s[i] == s[j]:
				sameCount = sameCount +1 
				j = j+1
			else:
				break
		sameCount += 1
		substrCount = substrCount + sameCount * (sameCount + 1)/2
		sameChar[j-1] = sameChar[j-1] + sameCount
		i=j
		
	k= n-2
	while(k>=0):
		if sameChar[k] == 0:
			sameChar[k] = sameChar[k+1]
		k-=1
	print(sameChar)
	
	#case 2
	i = 1
	while(i<n-1):
		if s[i]!=s[i-1] and s[i-1] == s[i+1]:
			substrCount = substrCount + min(sameChar[i-1], sameChar[i+1])
			if sameChar[i+1] > 1:
				i = i + sameChar[i+1]+1
			else:
				i+=1
		else:
			i+=1
		
	return int(substrCount)
				

if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	n = int(input())
	s = input()

	res = substrCount(n,s)
	
	fptr.write(str(res)+'\n')
	fptr.close()



    
    