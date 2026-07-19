class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        numSet = set(nums)

        for n in numSet:
            curr = 0
            if n - 1 not in numSet:
                curr = n
                while curr in numSet:
                    curr += 1
                
                best = max(best, curr - n)

        return best