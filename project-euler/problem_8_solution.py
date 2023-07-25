'''
Question link[Problem 8](https://www.hackerrank.com/contests/projecteuler/challenges/euler008/problem?isFullScreen=true)
'''

#!/bin/python3

import sys

def solution(number_string, k):
    n = len(number_string)
    max_product = 0
    for i in range(n - k + 1):
        product = 1
        for j in range(k):
            product *= int(number_string[i + j])
        max_product = max(max_product, product)
    return max_product

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(solution(num, k))
    