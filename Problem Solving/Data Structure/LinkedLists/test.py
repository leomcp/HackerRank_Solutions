class Node:
	def __init__(self, data):
		self.data = data
		self.next = None 

class LinkedList:
	def __init__(self):
		self.head = Node(None)
		self.size = 0 
	def insert(self, elem):
		node = Node(elem)
		curr_node = self.head
		while(curr_node.next != None):
			curr_node = curr_node.next
		curr_node.next = node
		self.size = self.size + 1 
	def reverse(self):
		prev_node = Node(None)
		curr_node = self.head
		while(curr_node.next != None):

	def printLL(self):
		elem = []
		curr_node = self.head
		while curr_node != None:
			elem.append(curr_node.data)
			curr_node = curr_node.next
		print(elem)

if __name__ == "__main__":
	ll = LinkedList()

	list = [1, 2, 3, 4]
	for elem in list:
		ll.insert(elem)
	ll.printLL()

