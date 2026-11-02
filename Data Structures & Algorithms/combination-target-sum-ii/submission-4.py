class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def back(i, cur, total):
            if total == target:
                res.append(cur[::])
                return
            if i == len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            back(i + 1, cur, total + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            back(i + 1, cur, total)
        back(0, [], 0)
        return res