from os import *
from sys import *
from collections import *
from math import *

from sys import stdin


def solve(ind, nums, dp):
    if ind == 0:
        return nums[ind]
    if ind < 0:
        return 0
    if dp[ind]!=-1:
        return dp[ind]
    pick = solve(ind-2, nums, dp) + nums[ind]
    notpick = solve(ind-1, nums, dp)
    dp[ind] = max(pick, notpick)
    return dp[ind]

def maximumNonAdjacentSum(nums):

    # Memoization 
    
    # Write your code here.
    # dp = [-1]*len(nums)
    # return solve(len(nums)-1, nums, dp)

    # Tabulation

    n = len(nums)
    dp = [0]*n
    dp[0] = nums[0]
    for i in range(1,n):
        pick = nums[i]
        if i>1:
            pick = dp[i-2] + nums[i]
        notpick = dp[i-1]
        dp[i] = max(pick, notpick)
    return dp[n-1]

# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    t -= 1