

class Node:

	def __init__(self, data=None):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = Node()
		self.size = 0 

	def add_Node(self, data):
		curr_node = self.head

		while curr_node.next != None:
			curr_node = curr_node.next
		curr_node.next = Node(data)
		self.size = self.size + 1 

	def print_LinkedList(self):
		curr_node = self.head 

		lllist = []

		while(curr_node != None):
			lllist.append(curr_node.data)
			curr_node = curr_node.next 

		print(lllist)

	def reverse_LinkedList(self):
		prev_node = None

		while True:
			curr_node = self.head.next
			if curr_node.next != None:
				next_curr_node = curr_node.next  
				self.head.next = next_curr_node
			curr_node.next = prev_node
			prev_node = curr_node
			if prev_node == self.head.next:
				break


	def get_Node(self, pos):
		req_node, curr_node, itr = self.head, self.head, 1

		while(curr_node!=None):
			if itr > pos:
				req_node = req_node.next 
			curr_node = curr_node.next
			itr = itr + 1

		return req_node.data 

if __name__ == "__main__":

	ll = LinkedList()

	for i in range(4):
		ll.add_Node(i)

	ll.print_LinkedList()

	#ll.reverse_LinkedList()

	#ll.print_LinkedList()

	print(ll.get_Node(2))



