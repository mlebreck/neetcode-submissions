class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1

        while l < r:
            check = target - numbers[l]
            if check in numbers:
                while numbers[r] != check:
                    r -= 1
                return [l + 1, r + 1]
            l += 1