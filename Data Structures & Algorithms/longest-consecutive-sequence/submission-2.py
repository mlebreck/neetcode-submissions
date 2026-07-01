class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num

                while current in num_set:
                    current += 1

                best = max(best, current - num)

        return best
