
'''
Nth prime number
Question link[Problem 7](https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem?isFullScreen=true)
'''


#!/bin/python3

import sys


def nth_prime(n):
    arr = [1]*(n*11)
    arr[0] = arr[1] = 0
    i = 3
    prime_count = 0
    for j in range(2, len(arr)):
        if arr[j] == 1:
            prime_count += 1
            if prime_count == n:
                return j
            for k in range(j*j, len(arr), j):
                arr[k] = 0
    return None


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(nth_prime(n))
