import os
import sys
import math
import random
import re

def _getMedian(arr):
	arr.sort()
	if len(arr) / 2:
		return (arr[len(arr)/2] + arr[len(arr)/ 2])/2
	else:
		return arr[len(arr)/2]
		
def activityNotifications(expenditure, d):
	notifications =0
	
	for i in range(d, len(expenditure)):
		
		start = i-d
		end = i-1
		arr = expenditure[start:end]
		median = _getMedian(arr)
		
		
		if arr[i] >= median:
			notifications += 1
	return notifications
		
	
print(activityNotifications([2,3,4,2,3,6,8,4,5],9))


