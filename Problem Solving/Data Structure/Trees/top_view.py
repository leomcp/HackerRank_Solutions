class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)"""
def level_order(root):
    q = []
    lvl_order = []
    
    q.append(root)
    
    while True:
        head = q[0]
        del(q[0])
        if head.left is not None:
            q.append(head.left)
        if head.right is not None:
            q.append(head.right)
        lvl_order.append(head.info)
        if len(q)==0:
            return lvl_order
            
def vertical_order(root):
    q = []
    vertical_order_map = {}
    
    q.append(root)
    root.level = 0 
    vertical_order_map["0"] = [root.info]
    
    while True:
        head = q[0]
        head_lvl = head.level
        del(q[0])
        
        if head.left is not None:
            q.append(head.left)
            head.left.level = head_lvl - 1
            if str(head.left.level) in vertical_order_map.keys():
                vertical_order_map[str(head.left.level)].append(head.left.info)
            else:
                vertical_order_map[str(head.left.level)] = [head.left.info]
            
        if head.right is not None:
            q.append(head.right)
            head.right.level = head_lvl + 1
            if str(head.right.level) in vertical_order_map.keys():
                vertical_order_map[str(head.right.level)].append(head.right.info)
            else:
                vertical_order_map[str(head.right.level)] = [head.right.info]
                
        if len(q) == 0:
            return vertical_order_map
            
        

def topView(root):
    #Write your code here
    lvl_order = level_order(root)
    # print(lvl_order)
    vertical_order_map = vertical_order(root)
    # print(vertical_order_map)

    for key in sorted(map(int, vertical_order_map.keys())):
        if len(vertical_order_map[str(key)]) > 1:
            for elem in vertical_order_map[str(key)]:
                if elem in lvl_order:
                    print(elem),
                    break
        else:
            print(vertical_order_map[str(key)][0]),
    print("")

                
    
        
      

tree = BinarySearchTree()
t = int(raw_input())

arr = list(map(int, raw_input().split()))

for i in xrange(t):
    tree.create(arr[i])
    
topView(tree.root)
