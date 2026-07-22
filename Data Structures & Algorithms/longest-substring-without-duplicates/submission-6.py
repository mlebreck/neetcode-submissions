class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cSet = set()
        l, r = 0, 1
        best = 0

        for r in range(len(s)):
            while s[r] in cSet:
                cSet.remove(s[l])
                l += 1
            cSet.add(s[r])
            best = max(best, r - l + 1)
        return best