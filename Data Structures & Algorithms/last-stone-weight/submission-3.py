class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            large = -heapq.heappop(heap)
            small = -heapq.heappop(heap)

            if large != small:
                heapq.heappush(heap, -(large - small))
        return -heap[0] if heap else 0