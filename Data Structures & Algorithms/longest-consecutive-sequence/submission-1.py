class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Use a set for O(1) membership checks and to ignore duplicates
        unique_nums = set(nums)
        longest_length = 0

        for start in unique_nums:
            # Only begin counting from the start of a sequence
            if (start - 1) not in unique_nums:
                # Walk forward to measure the streak length
                current = start
                streak_length = 0

                while current in unique_nums:
                    streak_length += 1
                    current += 1

                # Update the best (explicit comparison version)
                if streak_length > longest_length:
                    longest_length = streak_length

        return longest_length
