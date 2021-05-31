#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#
from collections import deque

class Vertex:
    
    def __init__(self, data):
        self.data = data
        self.distance = -1
        self.neighbours = []
        
    def addNeighbour(self, v):
        self.neighbours.append(v)
        
class UDGraph:
    
    def __init__(self, n, m, edges, s):
        self.vertices = {}
        
        self.n = n
        self.m = m
        self.edges = edges
        self.s = s
        
        self.build()
        self._bfs()
        
    def build(self):
        for n in range(1, self.n+1):
            self.vertices[n] = Vertex(n)
        for edge in self.edges:
            self._addEdge(edge[0], edge[1])
            
    def _addEdge(self, u, v):       
        self.vertices[u].addNeighbour(v)
        self.vertices[v].addNeighbour(u)
            
    def _bfs(self):
        q = deque()
        q.append(self.s)
        self.vertices[self.s].distance = 0
        
        while len(q)>0:
            head_v = q.popleft()
            
            for neighbour in self.vertices[head_v].neighbours:
                if self.vertices[neighbour].distance == -1:
                    self.vertices[neighbour].distance = self.vertices[head_v].distance + 6
                    q.append(neighbour)
                    
    def result(self):
        result = []
        for v in sorted(self.vertices):
            if v != self.s:
                result.append(self.vertices[v].distance)
        return result
                

def bfs(n, m, edges, s):
    # Write your code here
   udg = UDGraph(n, m, edges, s)
   return udg.result()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
