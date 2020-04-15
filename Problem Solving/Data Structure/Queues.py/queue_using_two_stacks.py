# Enter your code here. Read input from STDIN. Print output to STDOUT

class Stack:

	def __init__(self):
		self._data = []
		self._size = 0 

	def is_empty(self):
		return self._size == 0

	def size(self):
		return self._size

	def push(self, elem):
		self._data.append(elem)
		self._size = self._size + 1

	def pop(self):
		if not self.is_empty():
			del(self._data[-1])
			self._size = self._size - 1

	def top(self):
		if not self.is_empty():
			return self._data[-1]

class Queue:

	def __init__(self):
		self._s1 = Stack()
		self._s2 = Stack()

	def is_empty(self):
		return self._s1.is_empty() and self._s2.is_empty()

	def size(self):
		return self._s1.size() + self._s2.size()

	def enqueue(self, elem):
		self._s1.push(elem)

	def dequeue(self):
		if self._s2.is_empty():
			while not self._s1.is_empty():
				self._s2.push(self._s1.top())
				self._s1.pop()
		top = self._s2.top()
		self._s2.pop()
		return top 

	def front(self):
		if self._s2.is_empty():
			while not self._s1.is_empty():
				self._s2.push(self._s1.top())
				self._s1.pop()
		return self._s2.top()



if __name__ == "__main__":

	q = Queue()

	n = int(input())

	for _ in range(n):

		qa = input().split()

		if int(qa[0]) == 1:
			q.enqueue(int(qa[1]))
		elif int(qa[0]) == 2:
			q.dequeue()
		elif int(qa[0]) == 3:
			print(q.front())
