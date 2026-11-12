class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for x in nums:
            for t in range(target, x - 1, -1):
                if dp[t - x]:
                    dp[t] = True
        return dp[target]