class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_val = max_val = best = nums[0]
        for x in nums[1:]:
            candidates = (x, min_val * x, max_val * x)
            max_val, min_val = max(candidates), min(candidates)
            best = max(best, max_val)
        return best