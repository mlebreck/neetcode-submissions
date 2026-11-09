class Solution:
    def numDecodings(self, s: str) -> int:
        prev, cur = 1, (1 if s[0] != "0" else 0)
        for i in range(2, len(s) + 1):
            new = 0
            if s[i - 1] != "0":
                new += cur
            if 10 <= int(s[i-2:i]) <= 26:
                new += prev
            prev, cur = cur, new
        return cur