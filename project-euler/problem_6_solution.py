'''
Question link[Problem 6](https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem?isFullScreen=true)

s1 = 1^2 + 2^2 + 3^2 + ... + n^2 = n(n+1)(2n+1)/6
s2 = (1+2+3+...+n)^2 = [n(n+1)/2]^2
ans = abs(s2-s1)

'''

#!/bin/python3

import sys


def solution(n):
    s1 = (n*(n+1)*(2*n+1))//6
    s2 = ((n*(n+1))//2)**2
    return abs(s2-s1)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solution(n))
