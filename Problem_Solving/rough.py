#arr = [1, 2, 1, 3, 2]
#d = 3
#m = 2 

arr = [4]
d = 4
m = 1
for i in range(0, len(arr) - m + 1):
	for j in range(0, m):
		print(arr[i+j])