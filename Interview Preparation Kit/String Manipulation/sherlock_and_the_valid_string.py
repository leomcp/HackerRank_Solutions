import os
import re
import math
import random




def _allCharSame(list):
	flag = 1
	for i in list:
		if list[0] != i and i > 0:
			flag = 0
	return flag
	
def _getStrDict(s):
	strdict= {}
	for i in s:
		if i in strdict.keys():
			strdict[i] +=1
		else:
			strdict[i] = 1
	return strdict

def isValid(s):
	strfreq = _getStrDict(s)
	strfreqval = list(strfreq.values())
	
	
	if _allCharSame(strfreqval):
		return "YES"
	else:
		for idx, val in enumerate(strfreqval):
			prev = val
			strfreqval[idx]= val-1
			
			if _allCharSame(strfreqval):
				return "YES"
			else:
				strfreqval[idx] = prev
	
	return "NO"
	
if __name__ == "__main__":
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	s = input()

	res = isValid(s)
	fptr.write(str(res)+'\n')
	fptr.close()
    
    


    
    
