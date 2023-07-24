'''
Question link [Project Euler Problem 5](https://www.hackerrank.com/contests/projecteuler/challenges/euler005/problem?isFullScreen=true)
'''

#!/bin/python3

import sys

def euclidean_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a,b):
    return a*b//euclidean_gcd(a,b)

def solution(n):
    res = 1
    for i in range(2,n+1):
        res = lcm(res, i)
    return res
    
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solution(n))