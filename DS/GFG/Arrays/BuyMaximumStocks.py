#!/usr/bin/python3

# https://www.hackerrank.com/contests/gs-codesprint/challenges/buy-maximum-stocks

import sys

def buyMaximumProducts(n, k, a):
    valWithIndex = sorted(list(enumerate(a)), key=lambda x:x[1])
    stockCount = 0
    for index, price in valWithIndex:
        stocksBought = min(index+1, k//price)
        k -= stocksBought*price
        stockCount += stocksBought
    return stockCount

    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    k = int(input().strip())
    result = buyMaximumProducts(n, k, arr)
    print(result)