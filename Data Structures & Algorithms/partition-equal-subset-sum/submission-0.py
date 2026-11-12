class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False                                   # phase 1: an odd total has no half
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True                                       # phase 2 starts: only the empty pick
        for x in nums:                                     # one number at a time
            for t in range(target, x - 1, -1):             # downward, so each number is used once
                if dp[t - x]:
                    dp[t] = True
        return dp[target]                                  # phase 3: read the one cell that matters