'''
Question link [Project Euler Problem 2](https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem?isFullScreen=true)
'''

#!/bin/python3
import sys

def is_prime(n):
    # returns True if n is prime else returns False
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def solution(n):
    max_prime = 0
    for i in range(1, n+1):
        if n % i == 0:
            if is_prime(n//i):
                return n//i
                break


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solution(n))
