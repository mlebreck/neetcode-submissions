class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:                    # note: l < r, converge to one element
            m = (l + r) // 2
            if nums[m] > nums[r]:       # min is strictly right of mid
                l = m + 1
            else:                       # min is at mid or left of it
                r = m
        return nums[l]                  # l == r → the minimum