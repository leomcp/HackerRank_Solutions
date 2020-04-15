# Enter your code here. Read input from STDIN. Print output to STDOUT

class SimpleTextEditor:

	def __init__(self):
		self._S = ""
		self._data = []
		self._size = 0 

	def _addStack(self, prev_S):
		self._data.append(prev_S)
		self._size = self._size + 1 

	def _popStack(self):
		if self._size > 0:
			top = self._data[-1]
			del(self._data[-1])
			return top
		else:
			return 0 

	def appendString(self, string):
		self._addStack(self._S)
		self._S = self._S + string

	def deleteString(self, idx):
		self._addStack(self._S)
		self._S = self._S[:-idx]

	def printElem(self, idx):
		if len(self._S) >= idx:
			print(self._S[idx])
		else:
			return 0 

	def undo(self):
		self._S = self._popStack()


if __name__ == "__main__":

	ste = SimpleTextEditor()

	n = int(input())

	for i in range(n):

		qa = input().split()

		if int(qa[0]) == 1:
			string = str(qa[1])
			ste.appendString(string)
		elif int(qa[0]) ==2:
			idx = int(qa[1])
			ste.deleteString(idx)

		elif int(qa[0]) == 3:
			idx = int(qa[1])
			ste.printElem(idx-1)

		else:
			ste.undo()




		

