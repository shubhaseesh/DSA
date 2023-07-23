'''
question link https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem?isFullScreen=true
'''

#!/bin/python3

import sys


def solution(n):
    t3 = (n-1)//3
    t5 = (n-1)//5
    t15 = (n-1)//15
    s3 = 3*t3*(t3+1)//2
    s5 = 5*t5*(t5+1)//2
    s15 = 15*t15*(t15+1)//2
    return int(s3+s5-s15)


t = int(input().strip())
if t >= 1 and t <= 10**5:
    for a0 in range(t):
        n = int(input().strip())
        if n >= 1 and n <= 10**9:
            print(solution(n))
else:
    print(0)