class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i, n in enumerate(nums):
            check = target - n

            if check in index_map:
                return [index_map[check], i]
            
            index_map[n] = i