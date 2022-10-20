#!/usr/bin/python3

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        expectRes = 0
        while low<=high:
            mid = (low+high)//2
            midSquare = mid*mid
            if midSquare==x:
                return mid
            elif midSquare<x:
                expectRes = mid
                low = mid+1
            else:
                high = mid-1
        return expectRes

print(Solution().mySqrt(16))
