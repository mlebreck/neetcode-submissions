class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def back(i, cur, total):
            if total == target:
                res.append(cur[::])
                return
            if i == len(nums) or total > target:
                return
            
            cur.append(nums[i])
            back(i, cur, total + nums[i])
            cur.pop()
            back(i + 1, cur, total)
        back(0, [], 0)
        return res