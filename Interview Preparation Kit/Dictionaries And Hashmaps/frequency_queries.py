import math
import os
import random
import re
import sys



def freqQueries(queries):
	output =[]
	freq ={}
	count={}
	
	
	for opr, data in queries:
		#insert
		if opr==1:
			if data in freq.keys():
				count[freq[data]] =- 1
				freq[data] += 1
				if freq[data] in count.keys():
					count[freq[data]]+=1
				else:
					count[freq[data]]=1
			else:
				freq[data] = 1
				if freq[data] in count.keys():
					count[freq[data]] += 1
				else:
					count[freq[data]] = 1
				
		#delete		
		elif opr == 2:
			if data in freq.keys():
				if freq[data] > 0:
					count[freq[data]] -= 1
					freq[data] -= 1
					if freq[data] in count.keys():
						count[freq[data]] += 1
					else:
						count[freq[data]] = 1
					
			
		# check counts	
		elif opr == 3:
			if data in count.keys() and count[data] > 0:
				output.append(1)
			else:
				output.append(0)
	
	return output




#q = [(1,5),(1,6),(3,2),(1,10),(1,10),(1,6),(2,5),(3,2)]
#print(freqQueries(q))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = freqQueries( queries)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    
