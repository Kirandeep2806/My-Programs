#!/usr/bin/python3

# Partial Execution

from math import log10

for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    res = 0
    for number in range(a, b+1):
        count = 0
        product = 1
        sum = 0
        bound = int(log10(number)) + 1
        while count < bound:
            temp = number % 10
            product *= temp
            sum += temp
            number //= 10
            count += 1
        if not product%sum:
            res += 1
    print(f"Case #{_+1}: {res}")
