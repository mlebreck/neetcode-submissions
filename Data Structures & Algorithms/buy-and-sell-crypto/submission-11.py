class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = float('inf')
        maxP = 0

        for p in prices:
            minP = min(minP, p)
            maxP = max(maxP, p - minP)
        return maxP