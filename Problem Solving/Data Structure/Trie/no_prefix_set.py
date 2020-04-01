# Enter your code here. Read input from STDIN. Print output to STDOUT

class Node:
    def __init__(self, letter):
        self.letter = letter 
        self.children = {}
        self.isWord = False
class Trie:
    def __init__(self):
        self.root = Node("*")
    def buildTrie(self, word):
        curr_node = self.root 
        for idx, char in enumerate(word):
            if curr_node.isWord:
                return word
            elif idx == len(word)-1 and char in curr_node.children:  
                return word 
            elif char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.isWord = True 

if __name__ == "__main__":
    trie = Trie()
    wordsDict = {}
    isGoodSet = True 
    n = int(input())
    for i in range(n):
        word = input()
        badword = trie.buildTrie(word)
        if badword != None:
            print("BAD SET")
            print(badword)
            isGoodSet = False 
            break
    if isGoodSet:
        print("GOOD SET")

        
# Enter your code here. Read input from STDIN. Print output to STDOUT

class Node:
    def __init__(self, letter):
        self.letter = letter 
        self.children = {}
        self.isWord = False
class Trie:
    def __init__(self):
        self.root = Node("*")
    def buildTrie(self, word):
        curr_node = self.root 
        for idx, char in enumerate(word):
            if curr_node.isWord:
                return word
            elif idx == len(word)-1 and char in curr_node.children:  
                return word 
            elif char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.isWord = True 

if __name__ == "__main__":
    trie = Trie()
    wordsDict = {}
    isGoodSet = True 
    n = int(input())
    for i in range(n):
        word = input()
        badword = trie.buildTrie(word)
        if badword != None:
            print("BAD SET")
            print(badword)
            isGoodSet = False 
            break
    if isGoodSet:
        print("GOOD SET")

        
