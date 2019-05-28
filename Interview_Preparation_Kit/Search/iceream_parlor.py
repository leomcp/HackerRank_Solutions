#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def getCostTable(arr):
    costable = {}
    for idx, val in enumerate(arr):
        costable[val] = idx
    return costable 

def whatFlavors(cost, money):
    costable = getCostTable(cost)

    for idx, val in enumerate(cost):
        key = (money - val)
        idx2 = costable.get(key)
        if idx2!= None and idx != idx2:
            print(idx+1, idx2+1)
            break

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
