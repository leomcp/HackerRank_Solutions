"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    #Enter Your Code Here
    res = []
    curr_node = root 
    
    for c in s:
        if c == '0':
            curr_node = curr_node.left 
        else:
            curr_node = curr_node.right 
        if curr_node.left is None and curr_node.right is None:
            res.append(curr_node.data)
            curr_node = root 
            
    print("".join(res))
