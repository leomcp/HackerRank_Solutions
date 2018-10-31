#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    freq = {}
    
    for i in range (0, len(q)):
        freq[q[i]] = 0
        
    count = 0  
    too_chaotic = False 
    finished = False 
    
    while(finished != True):
        finished = True 
        for a in range (0, len(q) - 1):
            if q[a] > q[a+1]:
                freq[q[a]] += 1
                
                if freq[q[a]] > 2:
                    too_chaotic = True
                    finished = True 
                    break
                    
                count+=1 
                temp = q[a]
                q[a] = q[a+1]
                q[a+1] = temp
                finished = False 
                
            
    if too_chaotic:
        print('Too chaotic')
    else:
        print(count)
            
    
        

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
