'''
Question link[Problem 9](https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem?isFullScreen=true)
'''


# @ Todo optimise the code
def pythagorean_triplet(n):
    p = None
    for c in range(n//3, n//2):
        for b in range((n-c)//2, c):
            a = n - c - b
            if (c*c) == (a*a) + (b*b):
                p = a*b*c
                break
        if p:
            return p


print(pythagorean_triplet(12))
