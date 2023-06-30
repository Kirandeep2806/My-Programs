class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache  
        def solve(i,tar):
            if i == 0:
                return int(tar%coins[0]==0)
            np = solve(i-1, tar)
            p = 0
            if coins[i]<=tar:
                p = solve(i, tar-coins[i])
            return np+p
        return solve(len(coins)-1, amount)