import math
import os
import random
import re
import sys

def appendAndDelete(s,t,k):
	
	if (len(s) + len(t)) < k:
		return "Yes"
	else:
		commonchar = 0
		for i in range(0, min(len(s), len(t)),1):
			if s[i] == t[i]:
				commonchar +=1
			else:
				break
		print(commonchar)
				
		if k== (len(s)+len(t)-2*commonchar) :
			return "Yes"
		else :
			if k > (len(s) + len(t)) and (len(s)+len(t)-2*commonchar)==0:
				return "Yes"
			else:
				return "No"
	return commonchar


if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	s = input()
	t = input()
	k = int(input())
	
	result = appendAndDelete(s,t,k)
	fptr.write(str(result)+'\n')
	fptr.close()
