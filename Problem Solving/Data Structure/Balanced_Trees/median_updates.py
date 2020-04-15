#!/bin/python
def median(a,x):
    

N = int(input())
s = []
x = []
for i in range(0, N):
   tmp = input().strip().split(' ')
   a, b = [xx for xx in tmp]
   s.append(a)
   x.append(int(b))
median(s,x)