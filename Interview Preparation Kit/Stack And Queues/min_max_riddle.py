
class Stack:
	def __init__(self, data):
		self.data = data

	def get_top(self):
		return self.data[-1]

	def pop(self):
		top = self.data[-1]
		del(self.data[-1])
		
	def computeMap(self):
		numMin_for_maxWin = {}

		while(self.data!=[]):
			top = self.get_top()
			max_win_size = 0 
			idx = len(self.data)-1

			while(top<=self.data[idx] and idx>=0):
				max_win_size = max_win_size + 1
				idx = idx -1

			self.pop()
			offset = 0 
			if numMin_for_maxWin.keys():
				min_key = min(numMin_for_maxWin.keys())
				if top<min_key:
					offset = numMin_for_maxWin[min_key]
				

			if top in numMin_for_maxWin.keys():
				numMin_for_maxWin[top] = max(max_win_size+offset,numMin_for_maxWin[top])
			else:
				numMin_for_maxWin[top] = max_win_size+offset

		return numMin_for_maxWin


def riddle(arr):

	# Largest window a given number is minimum for 
	s = Stack(arr)
	numMin_for_maxWin = s.computeMap()
	print(numMin_for_maxWin)


if __name__ == "__main__":

	arr = [11, 2, 3, 14, 5, 2, 11, 12]

	print(riddle(arr))