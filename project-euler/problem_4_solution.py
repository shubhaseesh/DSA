'''
Question link [Project Euler Problem 4](https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem?isFullScreen=true)
'''

#!/bin/python3
import sys


def isPalindrome(num):
    return str(num) == str(num)[::-1]
    # if num < 0:
    #     return False
    # original_num = num
    # reverse_num = 0
    # while num > 0:
    #     last_num = num % 10
    #     reverse_num = reverse_num * 10 + last_num
    #     num //= 10
    # return original_num == reverse_num


def solution(LIMIT):
    res = 0
    for i in range(101, 1000):
        for j in range(121, 1000, (1 if i % 11 == 0 else 11)):
            p = i*j
            x = str(p)
            if x == x[::-1] and p < LIMIT:
                res = max(res, p)
    return res


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solution(n))
