
def solve(s):
	res = ""

	for word in s.split():
		print(word)
		word = word.capitalize()
		res = res + word + ""

	return res 


print(solve("amit trivedi lol"))
print(solve("123 433 j amit trivedi lol"))
print(solve("a m i t t r i v e d i l o l"))
print(solve("1 2 3 4 5 5  9"))


