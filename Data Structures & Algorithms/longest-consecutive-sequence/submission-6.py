class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        best = 0

        for n in numSet:
            if n - 1 not in numSet:
                curr = n
                
                while curr in numSet:
                    curr += 1
             
                best = max(best, curr - n)

        return best