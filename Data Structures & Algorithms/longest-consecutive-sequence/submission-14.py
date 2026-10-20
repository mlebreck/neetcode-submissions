class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        best = 0

        for n in nums:
            cur = 0
            if n - 1 not in numSet:
                cur = n
                while cur in numSet:
                    cur += 1
                best = max(best, cur - n)
        return best