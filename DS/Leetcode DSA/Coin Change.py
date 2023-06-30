from sys import maxsize
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def solve(i,tar):
            if i == 0:
                if tar%coins[0]==0:
                    return tar//coins[0]
                return maxsize
            np = solve(i-1, tar)
            p = maxsize
            if coins[i] <= tar:
                p = 1 + solve(i, tar-coins[i])
            return min(np, p)
        res = solve(len(coins)-1, amount)
        if res >= maxsize:
            return -1
        return res