class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minTillNw=prices[0]
        for i in range(1,prices.__len__()):
            profit=max(profit,prices[i]-minTillNw)
            minTillNw=min(minTillNw,prices[i])
        return profit