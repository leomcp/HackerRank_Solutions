#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.

class ArrayStack:
    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        return self._data[-1]

    def push(self, elem):
        self._data.append(elem)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            del(self._data[-1])

    def print_stack(self):
        print(self._data)


def isBalanced(s):
    stack = ArrayStack()

    bracketsDict = { ')':'(', '}':'{', ']':'['}

    for char in s:
        if char not in bracketsDict.keys():
            stack.push(char)
        else:    
            if stack.is_empty() or stack.top() != bracketsDict[char]:
                return "NO"            
            stack.pop()
    
    if stack.is_empty():
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result)

