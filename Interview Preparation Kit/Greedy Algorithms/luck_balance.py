import math
import os
import random
import re
import sys

#k= 3
#contest= [(5,1),(2,1),(1,1),(8,1),(10,0),(5,0)]



def luckBalance(k, contest):
	contest = sorted(contest, reverse = True)
	balance = 0
	for luck, is_imp in contest:
		if not is_imp:
			balance += luck
			continue
		if k > 0:
			balance+=luck
			k-=1
		else:
			balance-=luck
	return balance


#print(luckBalance(k, contest))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)
    fptr.write(str(result) + '\n')
    fptr.close()
