#!/usr/bin/python3

def findNearestSquareRoot(n):
    ans = -1
    low = 1
    high = n
    while low <= high:
        mid = (low+high)//2
        sqVal = mid*mid
        if sqVal == n:
            return mid
        elif sqVal > n:
            high = mid-1
        else:
            low = mid+1
            ans = mid
    return ans

n = int(input())
res = findNearestSquareRoot(n)
print(res)
