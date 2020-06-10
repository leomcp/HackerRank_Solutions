
#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

def _insert(self, data, curr_node):
    if curr_node.info > data:
        if curr_node.left is None:
            curr_node.left = Node(data)
        else:
            self._insert(data, curr_node.left)
    elif curr_node.info < data:
        if curr_node.right is None:
            curr_node.right = Node(data)
        else:
            self._insert(data, curr_node.right)
    else:
        print("Already inserted ...")

def insert(self, val):
    #Enter you code here.
    if self.root==None:
        self.root = Node(val)
        return self.root
    else:
        self._insert(val, self.root)
        return self.root 
