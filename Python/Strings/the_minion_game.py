
def minion_game(str):
	stuart, kevin = 0, 0
	vowels = ['A','E','I','O','U']
	
	for idx in range(len(str)):
		if str[idx] in vowels:
			kevin = kevin + len(str) - idx
		else:
			stuart = stuart + len(str) - idx
	if stuart > kevin:
		print("Stuart {}".format(stuart))
	elif stuart < kevin:
		print("Kevin {}".format(kevin))
	else:
		print("Draw")

#if __name__ == "__main__":
#	s = input()
#	minion_game(s)

