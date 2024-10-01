# https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem?isFullScreen=true
# https://projecteuler.net/problem=2
#!/bin/python3
import sys

def fibonacci(nums, n) -> int:
    evenSum = 0;
    sum = nums[-2] + nums[-1]
    while sum < n:
        if sum % 2 == 0:
            evenSum += sum
        nums.append(sum)
        sum = nums[-2] + nums[-1]
    return evenSum

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    nums = [1, 1]
    print(fibonacci(nums, n))
