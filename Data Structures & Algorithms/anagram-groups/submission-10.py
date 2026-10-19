class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sig = {}
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
            if key in sig:
                sig[key].append(s)
            else:
                sig[key] = [s]
        return list(sig.values())