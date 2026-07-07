class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i_map = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in i_map:
                return [i_map[diff], i]

            i_map[num] = i