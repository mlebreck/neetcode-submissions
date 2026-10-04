class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sig_map = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)

            sig_map[key].append(s)

        return list(sig_map.values())