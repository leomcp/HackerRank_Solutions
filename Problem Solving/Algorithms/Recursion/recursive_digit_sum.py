
def processNum(num, k):
	new_num = 0 
	for _ in range(k+1):
		new_num = new_num * pow(10, k+1) + num
	return new_num

def digit_sum(num):
	total = 0 
	while num > 0:
		mod = num%10
		num = num//10
		total = total + mod
	return int(total)

def superDigit(num, k):
	num = processNum(num, k)
	# dig_sum = digit_sum(num)
	return cal_sum(num)
	# return dig_sum

def cal_sum(num):
	if digit_sum>9:
		dig_sum = digit_sum(num)
		return cal_sum(dig_sum)
	else:
		return num

if __name__ == "__main__":

	print(superDigit(168, 2))
