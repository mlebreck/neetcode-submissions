class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sig_map = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)

            if key in sig_map:
                sig_map[key].append(s)
            else:
                sig_map[key] = [s]

        return list(sig_map.values())