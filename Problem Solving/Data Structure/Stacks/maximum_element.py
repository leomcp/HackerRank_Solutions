

class ArrayStack:

	def __init__(self):
		self._data = []
		self.max = 0 

	def __len__(self):
		return len(self._data)

	def is_empty(self):
		return len(self._data) == 0

	def get_max(self):
		return self.max

	def push(self, e):
		self._data.append(e)
		if self.max < e:
			self.max = e

	def pop(self):
		if self.is_empty():
			raise Empty('Stack is empty')
		else:
			delelem = self._data[-1]
			del(self._data[-1])
			if self.is_empty():
				self.max = 0 
			elif self.max == delelem:
				self._cal_max()


	def _cal_max(self):
		self.max = 0 
		for elem in self._data:
			if self.max < elem:
				self.max = elem

	def print_stack(self):
		print(self._data)


if __name__ == "__main__":
	"""
	stack = ArrayStack()

	stack.push(10)
	stack.push(20)
	stack.pop()
	stack.print_stack()
	stack.push(92)
	stack.push(1)
	stack.print_stack()
	print(stack.get_max())

	"""
	n = int(input())

	stack = ArrayStack()

	for i in range(n):

		oprval = input().rstrip().split()
		opr = int(oprval[0])
		if opr == 1:
			val = int(oprval[1])
			stack.push(val)
			
		elif opr ==2:
			stack.pop()
			
		elif opr == 3:
			print(stack.get_max())

	






