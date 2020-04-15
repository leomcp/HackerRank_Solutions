#!/bin/python3

import os
"""
class ArrayStack:

    def __init__(self):
        self._data = []
        self._size = int(0) 
        self._front = int(0) 

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size


    def getFirst(self):
        if self.is_empty():
            return 0 
        else:
            return self._data[self._front]


    def add_element(self, elem):
        self._data.append(elem)
        self._size = self._size + 1 

    def pop(self):
        if self.is_empty():
            return 0 
        else:
            self._data[self._front] = None 
            self._front = self._front + 1 
            self._size = self._size - 1

    def displayStack(self):
        print(self._data)
"""
class QueueStack:

    def __init__(self):
        self._data = []
        self._size = 0 
        self._front = 0 

    def is_empty(self):
        return self._size == 0 

    def __len__(self):
        return self._size

    def getFirst(self):
        if self.is_empty():
            return 0
        else:
            return self._data[self._front]

    def add_element(self, elem):
        self._data.append(elem)
        self._size = self._size + 1 

    def pop(self):
        if self.is_empty():
            return 0 
        else:
            self._data[self._front] = None
            self._front = self._front + 1
            self._size = self._size - 1

    def displayStack(self):
        print(self._data)


def twoStacks(k, a, b):
    sum , count = 0, 0 
    stackA = QueueStack()
    stackB = QueueStack()

    for i in a:
        stackA.add_element(i)
    for i in b:
        stackB.add_element(i)

    #stackA.displayStack()
    #stackB.displayStack()



    while(sum<=k):
        if stackA.getFirst() >= stackB.getFirst():
            sum = sum + stackA.getFirst()
            #print(stackA.getFirst(), stackB.getFirst(), sum, count)
            stackA.pop()
        else:
            sum = sum + stackB.getFirst()
            #print(stackA.getFirst(), stackB.getFirst(), sum, count)
            stackB.pop()  
        count = count + 1 
        #stackA.displayStack()
        #stackB.displayStack()

    return count



if __name__ == "__main__":

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for games in range(g):

        inp = list(map(int, input().rstrip().split()))

        n = int(inp[0])
        m = int(inp[1])
        x = int(inp[2])

        a = list(map(int, input().split()))

        b = list(map(int, input().split()))

        result = twoStacks(x, a, b)

        #print(result)
        fptr.write(str(result) + '\n')

    fptr.close()

