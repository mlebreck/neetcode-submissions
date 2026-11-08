class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = 0
        best = 0

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            if (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best
