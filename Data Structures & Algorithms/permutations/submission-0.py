class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perm, used):
            if len(perm) == len(nums):
                res.append(perm.copy())
            
            for i in range(len(nums)):
                if not used[i]:
                    perm.append(nums[i])
                    used[i] = True
                    backtrack(perm, used)
                    perm.pop()
                    used[i] = False
        backtrack([], [False] * len(nums))
        return res
                    