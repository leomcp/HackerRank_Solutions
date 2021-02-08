import sys
""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    if root is None:
        return True 
    else:
        max_v = sys.maxsize 
        min_v = -sys.maxsize
        return _validateBST(root, min_v, max_v)
    
def _validateBST(curr_node, min_v, max_v):
    if curr_node is None:
        return True 
    if (curr_node.data > min_v and
    curr_node.data < max_v and 
    _validateBST(curr_node.left, min_v, curr_node.data) and
    _validateBST(curr_node.right, curr_node.data, max_v)):
        return True
    else:
        return False """ Node is defined as
