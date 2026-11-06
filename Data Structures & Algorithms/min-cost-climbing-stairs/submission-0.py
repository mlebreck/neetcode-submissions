class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, cur = 0, 0
        for i in range(2, len(cost) + 1):
            prev, cur = cur, min(cur + cost[i - 1], prev + cost[i - 2])
        return cur