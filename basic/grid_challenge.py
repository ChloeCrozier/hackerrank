# https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four
#!/bin/python3
import math
import os
import random
import re
import sys

def checkCols(grid):
    length = len(grid[0])
    for col in range(0, length):
        prev = grid[0][col]
        for row in range(1, length):
            curr = grid[row][col]
            if prev > curr:
                return 'NO'
            prev = curr
    return 'YES'      

def gridChallenge(grid):
    for row in grid:
        (''.split(row)).sort()
    return checkCols(grid)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
