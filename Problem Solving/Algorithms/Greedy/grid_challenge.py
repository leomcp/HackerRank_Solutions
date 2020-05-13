#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.

class GridChallenge:

    def __init__(self, grid, n):
        self.grid = grid
        self.n = n

    def sort_rows(self):
        for row, seq in enumerate(grid):
            self.grid[row] = sorted(seq)
        return self.grid 

    def check(self):
        sorted_grid = self.sort_rows()
        for idx in range(self.n):
            col_grid = []
            for col in range(len(self.grid)):
                col_grid.append(self.grid[col][idx])
            # print(col_grid, sorted(col_grid))
            if col_grid == sorted(col_grid):
                pass
            else:
                return "NO"
        return "YES"


def gridChallenge(grid, n):
    gc = GridChallenge(grid, n)
    return gc.check()
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            
            grid.append(grid_item)

        l = len(grid[n-1])

        result = gridChallenge(grid, l)

        fptr.write(result + '\n')

    fptr.close()
