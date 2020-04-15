class Stack:
	def __init__(self):
		self._data = []
		self._size = 0 

	def is_empty(self):
		return self._size == 0 

	def __len__(self):
		return self._size

	def peek(self):
		return self._data[-1]

	def push(self, elem):
		self._data.append(elem)
		self._size = self._size + 1

	def pop(self):
		if self.is_empty():
			return -1
		else:
			top = self._data[-1]
			del(self._data[-1])
			self._size = self._size - 1
			return top 

	def printStack(self):
		print(self._data)

def largestRectangle(hist):

	posStack = Stack()
	hStack = Stack()
	maxArea = 0 

	for pos, hgt in enumerate(hist):
		if pos ==0 or hStack.peek() < hgt:
			posStack.push(pos)
			hStack.push(hgt)

		if pos == len(hist)-1:
			print(pos)
			posStack.printStack()
			hStack.printStack()

			while(hStack.__len__() > 0 ):
				area = hStack.pop()*(pos-posStack.pop()+1)
				print(area)
				if area >= maxArea:
					maxArea = area 
	return maxArea

if __name__ == "__main__":

	maxArea = largestRectangle([1, 2, 3, 4, 5])
	print("M:", maxArea)


			





