class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        signature_map = {}

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord('a')] += 1

            signature = tuple(count)

            if signature in signature_map:
                signature_map[signature].append(s)
            else:
                signature_map[signature] = [s]

        return list(signature_map.values())

