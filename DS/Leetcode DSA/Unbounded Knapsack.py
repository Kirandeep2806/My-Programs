from os import *
from sys import *
from collections import *
from math import *

def unboundedKnapsack(n, w, profit, weight):
    dp = [[0 for _ in range(w+1)] for __ in range(n)]
    def solve(i,val):
        if i==0:
            return profit[0]*(val//weight[0])
        if dp[i][val]!=0:
            return dp[i][val]
        notpick = solve(i-1,val)
        pick = 0
        if weight[i] <= val:
            pick = profit[i] + solve(i, val-weight[i])
        dp[i][val] = max(pick, notpick)
        return dp[i][val]
    return solve(n-1, w)


for _ in range(int(input())):
    n,w = list(map(int, input().split()))
    profit = list(map(int, input().split()))
    weight = list(map(int, input().split()))
    res = unboundedKnapsack(n,w,profit,weight)
    print(res)
