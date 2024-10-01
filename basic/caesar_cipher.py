# https://www.hackerrank.com/challenges/one-week-preparation-kit-caesar-cipher-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-three
#!/bin/python3
import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    res = []
    k = k % 26
    for char in s:
        if char.isalpha():
            if char.islower():
                shiftedChar = chr(((ord(char) + k - ord('a')) % 26) + ord('a'))
            else:
                shiftedChar = chr(((ord(char) + k - ord('A')) % 26) + ord('A'))
            res.append(shiftedChar)
        else:
            res.append(char)
    return ''.join(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
