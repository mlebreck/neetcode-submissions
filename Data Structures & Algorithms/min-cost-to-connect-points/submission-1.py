class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        heap = [(0,0)]
        visited = set()
        total = 0

        while len(visited) < n:
            cost, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            total += cost
            for v in range(n):
                if v not in visited:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(heap, (dist, v))
        return total