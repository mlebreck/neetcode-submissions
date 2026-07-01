class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i, num in enumerate(nums):
            check = target - num

            if check in index_map:
                return [index_map[check], i] 
        
            index_map[num] = i