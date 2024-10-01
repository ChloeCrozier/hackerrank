#!/bin/python3
import sys

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    
    sum = 0
    for i in range(0, n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)
