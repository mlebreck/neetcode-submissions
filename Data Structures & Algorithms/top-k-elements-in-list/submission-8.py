class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num,freq in freq.items():
            buckets[freq].append(num)

        res = []
        for f in range(len(buckets) -1, 0, -1):
            for num in buckets[f]:
                res.append(num)
                if len(res) == k:
                    return res