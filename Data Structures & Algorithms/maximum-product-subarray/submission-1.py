class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = best = nums[0]
        for x in nums[1:]:
            candidates = (x, cur_max * x, cur_min * x)
            cur_max, cur_min = max(candidates), min(candidates)
            best = max(best, cur_max)
        return best