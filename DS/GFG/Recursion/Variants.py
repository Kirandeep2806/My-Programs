#!/usr/bin/python3

# Find the number of minimum steps to reach n from m by using only the following operations:
# 1. Divide by 2
# 2. Divide by 3

from sys import maxsize

n = int(input() or "60")
m = int(input() or "51840")

def minSteps(n, m, steps=0):
    if m == n:
        return steps
    if m < n:
        return maxsize
    if m%3 == 0:
        stepsWith3 = minSteps(n, m//3, steps+1)
    else:
        stepsWith3 = maxsize
    if m%2 == 0:
        stepsWith2 = minSteps(n, m//2, steps+1)
    else:
        stepsWith2 = maxsize
    return min(stepsWith2, stepsWith3)

print(minSteps(n, m, 0))

# The above is the recursive solution and is also the minimization problem.
# So, we can use DP to optimize it.
