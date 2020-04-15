
class Node:
	def __init__(self, letter):
		self.letter = letter
		self.children = {}
		self.isWord = False

class AutoCompleteWords:
	def __init__(self):
		self.root = Node("*")
		self.result = []

	def buildTrie(self, wordsArr):
		for word in wordsArr:
			curr_node = self.root

			for letter in word:
				if letter not in curr_node.children:
					curr_node.children[letter] = Node(letter)
				curr_node = curr_node.children[letter]
			curr_node.isWord = True 

	def _getNode(self, prefix):
		curr_node = self.root 
		for char in prefix:
			if char in curr_node.children:
				curr_node = curr_node.children[char]
			else:
				return 
		return curr_node 

	def _findChildren(self, node, prefix):
		if node.isWord:
			self.result.append(prefix)
		if node.children:
			for child in node.children:
				prefix = prefix + child 
				print(prefix)
				self._findChildren(node.children[child], prefix)
		


	def autocomplete(self, prefix):
		node = self._getNode(prefix)
		if node:
			self._findChildren(node, prefix)



if __name__ == "__main__":

	words = ["dog", "dark", "cat", "door", "dodge"]
	prefix = "do"

	auto = AutoCompleteWords()
	auto.buildTrie(words)
	auto.autocomplete(prefix)

	print(auto.result)

	

