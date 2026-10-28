class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def back(perm, used):
            if len(perm) == len(nums):
                res.append(perm[::])
                return 
            
            for i in range(len(nums)):
                if not used[i]:
                    perm.append(nums[i])
                    used[i] = True
                    back(perm, used)
                    perm.pop()
                    used[i] = False
        back([], [False] * len(nums))
        return res
            
            