class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sig_map = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            sig = tuple(count)

            if sig in sig_map:
                sig_map[sig].append(s)
            else:
                sig_map[sig] = [s]

        return list(sig_map.values())