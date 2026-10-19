class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}

        for i,n in enumerate(nums):
            diff = target - n

            if diff in idx:
                return [idx[diff], i]
            idx[n] = i