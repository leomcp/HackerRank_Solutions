class Node:
	def __init__(self, char):
		self.char = char 
		self.children = {}
		self.isName = False 

class ContactTrie:
	def __init__(self):
		self.root = Node("*")
		self.counts = 0 

	def addContact(self, name):
		curr_node = self.root 

		for char in name:
			if char not in curr_node.children:
				curr_node.children[char] =  Node(char)
			curr_node = curr_node.children[char]
		curr_node.isName = True


	def _getNode(self, prefix):
		curr_node = self.root 

		for char in prefix:
			if char in curr_node.children:
				curr_node = curr_node.children[char]
			else:
				return 
		return curr_node

	def _countNode(self, node):
		if node.isName:
			self.counts = self.counts + 1
		if node.children:
			for child in node.children:
				self._countNode(node.children[child])
		

	def findCount(self, prefix):
		node = self._getNode(prefix)
		if node:
			self._countNode(node)


def contact(arr):
	trie = ContactTrie()
	result = []
	for row in range(len(arr)):
		trie.counts = 0 
		if arr[row][0] == "add":
			trie.addContact(arr[row][1])
		if arr[row][0] == "find":
			trie.findCount(arr[row][1])
			result.append(trie.counts)
	return result 

arr = [['add', 'hack'], ['add', 'hackerrank'], ['find', 'hac'], ['find', 'hak']]
print(contact(arr))
		