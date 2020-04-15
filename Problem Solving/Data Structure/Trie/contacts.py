#!/bin/python3

import os
import sys

#
# Complete the contacts function below.
#
class Node:
    def __init__(self, char):
        self.char = char 
        self.children = {}
        self.noNames = 0 

class Trie:
    def __init__(self):
        self.root = Node("*")
    def addName(self, name):
        curr_node = self.root
        for char in name:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
            curr_node.noNames = curr_node.noNames + 1
    def countName(self, name):
        curr_node = self.root 
        for idx, char in enumerate(name):
            if char in curr_node.children:
                if idx == len(name)-1:
                    return curr_node.noNames
                else:
                    curr_node = curr_node.children[char]

def contacts(queries):
    result = []
    trie = Trie()
    for list in queries:
        if list[0] == "add":
            trie.addName(list[1])
        elif list[0] == "find":
            noNames = trie.countName(list[1])
            if noNames == None:
                result.append(0)
            else:
                result.append(noNames)         
    return result 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    queries_rows = int(input())
    queries = []
    for _ in range(queries_rows):
        queries.append(input().rstrip().split())
    result = contacts(queries)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
