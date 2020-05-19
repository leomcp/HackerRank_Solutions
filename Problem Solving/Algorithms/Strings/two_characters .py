import itertools 

if __name__ == "__main__":

	# n = int(input())
	# s = str(input())

	s = 'beabeefeab'

	combinations = []
	for idx in range(len(s)-1):
		if s[idx]!=s[idx+1]:
			l = []
			l.append(s[idx])
			l.append(s[idx+1])
			if l not in combinations:
				combinations.append(l)
	print(combinations)

	for items in combinations:
		x = ""
		for char in s:
			if char not in items:
				x = x+char
		print(x)

