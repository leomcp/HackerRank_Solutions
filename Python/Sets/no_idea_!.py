
if __name__ == "__main__":

	n_m = input().split()
	n = n_m[0]
	m = n_m[1]

	arr = input().split()

	set_A = set(input().split())
	set_B = set(input().split())

	#print(n, m, arr, set_A, set_B)

	happiness = 0

	for item in arr:
		if item in set_A:
			happiness = happiness + 1
		elif item in set_B:
			happiness = happiness - 1 

	print(happiness)

