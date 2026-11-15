class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_n = max_n = best = nums[0]

        for x in nums[1:]:
            candidates = (x, min_n * x, max_n * x)
            max_n, min_n = max(candidates), min(candidates)
            best = max(best, max_n)
        return best