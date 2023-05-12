#!/usr/bin/python3

def solve(ind, target, arr, dp):
    if target == 0:
        return True
    if ind == 0:
        return arr[ind] == target
    if dp[ind][target] != -1:
        return dp[ind][target]
    pick = False
    if target >= arr[ind]:
        pick = solve(ind - 1, target - arr[ind], arr, dp)
    notPick = solve(ind - 1, target, arr, dp)
    dp[ind][target] = pick or notPick
    return dp[ind][target]

arr = [2,3,1,1]
target = 7
dp = [[-1 for _ in range(target+1)] for __ in range(len(arr))]
print(solve(len(arr)-1, target, arr, dp))

