#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def get_all_substring(s):
    l = len(s)
    alist = []
    for i in range(l):
        for j in range(i, l):
            alist.append(s[i:j+1])
    return alist

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return 0 
    
    s1 = Counter(str1)
    s2 = Counter(str2)
    
    for i in range(len(str1)):
        if s1[str1[i]] != s2[str1[i]]:
            return 0
    return 1 
    
  
# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    
    alist = get_all_substring(s)
    l = len(alist)
    counter = 0
    for i in range(l-1):
        for j in range (i+1, l):
            if is_anagram(alist[i], alist[j]):
                counter += 1
                
    return counter
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
