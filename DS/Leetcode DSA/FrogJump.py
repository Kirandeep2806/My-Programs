#!/usr/bin/python3

from os import *
from sys import *
from collections import *
from math import *

from typing import *

def solve(i, height, dp):
    if  i == 0:
        return 0
    if dp[i]!=-1:
        return dp[i]
    left = solve(i-1, height, dp) + abs(height[i] - height[i-1])
    right = float("inf")
    if i>1:
        right = solve(i-2, height, dp) + abs(height[i] - height[i-2])
    dp[i] = min(left, right)
    return dp[i]

def frogJump(n: int, heights: List[int]) -> int:

    # Memoization

    dp = [-1] * n
    res = solve(n-1, heights, dp)
    return res

    # Tabulation

    # def frogJump(n: int, heights: List[int]) -> int:
    # dp = [0] * n
    # for i in range(1,n):
    #     left = dp[i-1] + abs(heights[i] - heights[i-1])
    #     right = float("inf")
    #     if i>1:
    #         right = dp[i-2] + abs(heights[i] - heights[i-2])
    #     dp[i] = min(left, right)
    # return dp[n-1]
