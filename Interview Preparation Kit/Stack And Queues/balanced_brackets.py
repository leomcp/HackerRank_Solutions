
def is_balanced(mystr):
	bracketMap = {'{':'}','[':']','(':')'}

	stack = []

	for char in mystr:
		if char in bracketMap.keys():
			stack.append(char)
		elif bracketMap[stack[len(stack)-1]] == char:
			stack.pop()
		else:
			print('NO')
	if len(stack) == 0:
		print('YES')



if __name__ == "__main__":
	str1 = "{[()]}"
	str2 = "[(])"

	is_balanced(str1)
	is_balanced(str2)
