import math
import os
import random
import re
import sys

def testAnagram(str1, str2):
	if sorted(str1) == sorted(str2):
		return 1
	else:
		return 0
	
def sherlockAndAnagram(s):
	anagramCount = 0
	substr = {}
	strlen = len(s)
	for strsize in range(1,strlen):
		for i in range(0, strlen-strsize+1):
			end = i+strsize
			enterstr =(s[i:end])
			substr.setdefault(strsize, []).append(enterstr)	
	for key in substr.keys():
		arrcheck = substr[key]
		print(arrcheck)
		for i, val in enumerate(arrcheck):
			for j in range (i+1, len(arrcheck)):
				anagramCount = anagramCount + testAnagram(val,arrcheck[j])
	return anagramCount
	
if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	q = int(input())
	for q_itr in range(q):
		s = input()
		result = sherlockAndAnagram(s)
		fptr.write(str(result)+'\n')
	fptr.close()
