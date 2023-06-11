#!/usr/bin/python3

def maxProfit(values, weights, n, w):
    dp = [[-1 for _ in range(w+1)] for _ in range(n)]
    def solve(n, w):
        if n == 0:
            if weights[0] <= w:
                return values[0]
            return 0
        if dp[n][w]!=-1:
            return dp[n][w]
        pick = 0
        if (w-weights[n]) >= 0:
            pick = values[n] + solve(n - 1, w - weights[n])
        notpick = solve(n - 1, w)
        dp[n][w] = max(pick, notpick)
        return dp[n][w]
    return solve(n-1, w)

n = int(input())
n,w = list(map(int, input().split()))
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

res = maxProfit(values, weights, n, w)
print(res)
