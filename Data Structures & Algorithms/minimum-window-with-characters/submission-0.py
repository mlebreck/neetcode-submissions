from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)          # how many of each char t requires
        required = len(t)          # total chars still needed (counts duplicates)
        l = 0
        best = (float('inf'), 0, 0)   # (length, left, right) of best window so far

        for r, c in enumerate(s):
            if need[c] > 0:            # this char is still needed → it counts
                required -= 1
            need[c] -= 1               # every char decrements (may go negative = surplus)

            while required == 0:        # window is valid → try to shrink
                if r - l + 1 < best[0]:
                    best = (r - l + 1, l, r)
                need[s[l]] += 1                 # give back the left char
                if need[s[l]] > 0:             # we gave back something actually needed
                    required += 1              # window no longer valid → stop shrinking
                l += 1

        return "" if best[0] == float('inf') else s[best[1]:best[2] + 1]