'''
Question link [Project Euler Problem 10](https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem?isFullScreen=true)
'''

#!/bin/python3

import sys

# Todo optimise 
def sum_primes(n):
    s = 0
    arr = [1]*(n+1)
    arr[0], arr[1] = 0, 0

    for i in range(2, n+1):
        if arr[i] == 1:
            s += i
            for j in range(i*i, n+1, i):
                arr[j] = 0
    return s


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum_primes(n))
