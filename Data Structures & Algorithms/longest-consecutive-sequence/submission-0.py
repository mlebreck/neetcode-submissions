class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0

        # Iterate over unique values only (duplicates are irrelevant)
        for num in s:
            # Start-of-chain check: only begin if x-1 isn't present
            if num - 1 not in s:
                # Count length of the chain starting at x
                curr = num

                while curr in s:
                    curr += 1
        
                best = max(best, curr - num)

        return best
