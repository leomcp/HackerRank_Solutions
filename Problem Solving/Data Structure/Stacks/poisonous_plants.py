#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
class Stack:
	def __init__(self):
		self.data = []
		self.size = 0
	
	def peek(self):
		return self.data[-1]
		
	def front(self):
		return self.data[0]

	def push(self, elem):
		self.data.append(elem)
		self.size = self.size + 1

	def pop(self):
		if self.size != 0:
			del(self.data[-1])
			self.size = self.size - 1

	def remove_front(self):
		if self.size != 0:
			del(self.data[0])
			self.size = self.size - 1

	def erase_data(self):
		self.data = []
		self.size = 0 

	def printStack(self):
		print(self.data)

def merge(s1, s2):
	s1.printStack()
	s2.printStack()
	for elem in s2:
		s1.push(elem) 

def merge_stacks(list_of_stacks):

	merge = False 
	for idx, stack in enumerate(list_of_stacks):
		if stack.size == 0:
			del(list_of_stacks[idx])

	for stack in list_of_stacks:
		stack.printStack()
	print(len(list_of_stacks))

	start = len(list_of_stacks)-1
	
	for idx in range(start, 0):
		s1 = list_of_stacks[idx-1]
		s2 = list_of_stacks[idx]
		if s1.peek() >= s2.front():
			for elem in s2.data:
				print(elem)
				s1.push(elem)
			#del(list_of_stacks[idx])

	return list_of_stacks


def poisonousPlants(p):
	days = 0 
	list_of_stacks = []
	curr_stack = Stack()
	curr_stack.push(p[0])

	for idx in range(1, len(p)):
		if curr_stack.peek() > p[idx]:
			curr_stack.push(p[idx])
		else:
			list_of_stacks.append(curr_stack)
			curr_stack = Stack()
			curr_stack.push(p[idx])
	list_of_stacks.append(curr_stack)

	loopit = True 

	while loopit:
		
		for idx, stack in enumerate(list_of_stacks):
			if idx != 0 and stack.size != 0:
				stack.remove_front()

		list_of_stacks = merge_stacks(list_of_stacks)
		days = days + 1

		if len(list_of_stacks) == 1:
			loopit = False 

	return list_of_stacks, days 


if __name__ == '__main__':
    """fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()

    """
    list = [6, 5, 8, 4, 7, 10, 9]
    list_of_stacks, days = poisonousPlants(list)

    

    for stack in list_of_stacks:
    	stack.printStack()

    print(int(days-1))