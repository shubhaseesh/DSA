'''
Question link[Problem 9](https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem?isFullScreen=true)
'''


# @ Todo optimise the code
def pythagorean_triplet(n):
    for c in range(n//3, n//2):
        for b in range((n - c + 1) // 2,c):
            a = n - b - c
            if a*a + b*b == c*c:
                return a * b * c
    return -1


print(pythagorean_triplet(12))
print(pythagorean_triplet(30))
print(pythagorean_triplet(56))
print(pythagorean_triplet(121))