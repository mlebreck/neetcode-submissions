class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robLine(houses):
            prev, cur = 0, 0
            for money in houses:
                prev, cur = cur, max(cur, prev + money)
            return cur
        return max(robLine(nums[:-1]), robLine(nums[1:]))