class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob(houses):
            prev, cur = 0, 0
            for money in houses:
                prev, cur = cur, max(cur, prev + money)
            return cur
        
        return max(rob(nums[:-1]), rob(nums[1:]))