class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_map = {}
        
        for n in nums:
            f_map[n] = 1 + f_map.get(n, 0)

        buckets = [[] for _ in range(len(nums) + 1)]

        for n, freq in f_map.items():
            buckets[freq].append(n)

        res = []
        for freq_index in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq_index]:
                res.append(num)
                if len(res) == k:
                    return res 