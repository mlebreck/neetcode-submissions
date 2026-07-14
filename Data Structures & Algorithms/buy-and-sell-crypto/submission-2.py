class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxP = 0

        for p in prices:
            minPrice = min(minPrice, p)
            maxP = max(maxP, p - minPrice)
        return maxP
        