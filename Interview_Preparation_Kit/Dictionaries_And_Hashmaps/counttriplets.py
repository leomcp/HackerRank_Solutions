arr = [1, 3, 9, 9, 27, 81]

r = 3 

def _getRank(arr):
	rank = {}

	for i in arr:
		if i in rank.keys():
			rank[i] = rank[i] + 1
		else:
			rank[i] = 1
	return rank

def _check(arr):
	check = {}
	for i in arr.keys():
		check[i] = 0
	return check


def countTripplet(arr, r):
	rank = _getRank(arr)
	check = _check(rank)

	count = 0 
	for i in range(0, len(arr) -2):
		if check[arr[i]] == 0 :
			cost = 0 
			n1 = arr[i]
			n2 = n1 * r
			n3 = n2 * r

			if n1 in rank.keys():
				if n2 in rank.keys():
					if n3 in rank.keys():
						cost = rank[n1] * rank[n2] * rank[n3]
			count = count + cost
			check[arr[i]] = 1
			#print(check, rank)
			
	return count

print(countTripplet(arr, r))
print(countTripplet([1, 2, 2, 4], 2))
print(countTripplet([1, 3, 9, 9, 27, 81], 3))
print(countTripplet([1, 5, 5, 25, 125], 5))
