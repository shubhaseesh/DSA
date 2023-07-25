'''
Question link [Project Euler Problem 2](https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem?isFullScreen=true)
'''
# f = [1,2,3,5,8,13,21,34,55,89,144,233]
# n = 100
# sum = 2 + 8 + 34 = 44
#!/bin/python3

import sys


def solution(n):
    # n = 10
    a = 1
    b = 2
    s = b
    while True:
        c = a + b
        if c > n:
            break
        if c % 2 == 0 and c < n:
            s += c
        a = b
        b = c
    return s


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solution(n))
