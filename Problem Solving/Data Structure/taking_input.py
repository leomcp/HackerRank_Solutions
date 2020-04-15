def _isPrime(num):
	isPrime = False 
	for i in range(2, num):
		isPrime = False 
		if (num % i) == 0:
			break
		else:
			isPrime = True 
	return isPrime
	
def _get_prime_nums(n):
	result = [2,]
	if n >3:
		for i in range(3,n):
			if _isPrime(i):
				result.append(i)
	else:
		return []
	return result

def _get_prime_subsets(arr):
	

def prime_subset_sums(n):
	primeArr = _get_prime_nums(n)
	if len(primeArr) > 0:
		primesubsetArr = _get_prime_nums(primeArr)

	return primeArr

if __name__ == "__main__":

	k = int(input())
	
	for i in range(k):
		n = int(input())
		print(prime_subset_sums(n))




		
	