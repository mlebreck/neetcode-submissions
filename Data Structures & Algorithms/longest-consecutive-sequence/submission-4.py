class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0

        for num in nums:
            if num - 1 not in num_set:
                curr = num

                while curr in num_set:
                    curr += 1

                best = max(best, curr - num)

        return best