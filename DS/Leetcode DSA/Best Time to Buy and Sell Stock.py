class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minVal = 10**5+1
        for i in range(len(prices)):
            res = max(res, prices[i] - minVal)
            minVal = min(minVal, prices[i])
        return res
