# https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem?isFullScreen=true
# https://projecteuler.net/problem=1
#!/bin/python3
import sys

def sum(divisor, upperRange):
    multiples = (upperRange - 1) // divisor
    return divisor * ((multiples * (multiples + 1)) // 2)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum(3, n) + sum(5, n) - sum(15, n))
