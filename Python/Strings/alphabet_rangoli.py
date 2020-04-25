
def print_rangoli(size):
	if size<=0 or size>26:
		return 

	alpha = "abcdefghijklmnopqrstuvwxyz"
	center = alpha[size-1]
	width = size*4-3
	n_char = 1 


	for i in range(1, size*2):
		if i<size:
			n_dashes = width-n_char
			print("-"*int(n_dashes/2)+center+"-"*int(n_dashes/2))
			if i!=size:
				n_char = n_char + 4
				center = ""
				idx = size-1
				for j in range(int(n_char/2)):
					center = center+alpha[idx]+"-"
					idx = idx -1
				s = center[:-3]
				center = center + s[::-1]
		elif i == size:
			center = ""
			idx = size-1 
			for i in range(size):
				center = center+alpha[idx]+"-"
				idx = idx-1 
			s = center[:-3]
			center = center + s[::-1]
			print(center)
			n_char = n_char - 4
			n_dashes = width-n_char
		else:
			n_char = n_char - 4
			n_dashes = width-n_char
			if int(n_char/2)==0:
				center = alpha[size-1]+"-"
			else:
				center = ""
				idx = size-1 
				for j in range(int(n_char/2)):
					center = center+alpha[idx-1]+"-"
					idx = idx -1 
				s = center[:-3]
				center = center + s[::-1]
			print("-"*int(n_dashes/2)+center+"-"*int(n_dashes/2))







if __name__ == "__main__":

	#n = int(input())
	print_rangoli(5)
