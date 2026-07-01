class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        signature_map = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)

            if key in signature_map:
                signature_map[key].append(s)
            else:
                signature_map[key] = [s]

        return list(signature_map.values())
