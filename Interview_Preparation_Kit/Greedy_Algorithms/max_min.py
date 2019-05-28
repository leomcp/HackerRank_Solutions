import sys 

arr = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]
k = 4 

def maxMin(k, arr):
	
	arr.sort()
	print(arr)
	unfairness = sys.maxint 
     
	last = len(arr) - k + 1
	
	for i in range(0, last):
		maxNo = -sys.maxint
		minNo = sys.maxint
		for j in range(0, k):
			
			if arr[i+j] > maxNo:
				maxNo = arr[i + j]
			if arr[i+j] < minNo:
				minNo = arr[i+j]

		cal = maxNo - minNo
		

		if unfairness > cal:
			unfairness = cal
		print(maxNo, minNo, cal, unfairness)
	return unfairness

print(arr)
print("-" * 40)
print(maxMin(k, arr))