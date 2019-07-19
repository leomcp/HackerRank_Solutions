#!/bin/python
import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
	machines.sort()
	low_rate = machines[0]
	high_rate =  machines[-1]
	print(low_rate, high_rate)
	lowerBound = (goal//(len(machines)/low_rate))
	upperBound = (goal//(len(machines)/high_rate)) + 1

	print(lowerBound, upperBound)

machines = [4, 5, 6]
goal = 12 

print(minTime(machines, goal))

