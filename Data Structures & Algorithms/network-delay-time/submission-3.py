class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        INF = float('inf')
        dist = {i : INF for i in range(1, n + 1)}
        dist[k] = 0
        q = deque([(0, k)])

        while q:
            cost, u = q.popleft()
            if cost > dist[u]:
                continue
            for v, w in adj[u]:
                if cost + w < dist[v]:
                    dist[v] = cost + w
                    q.append((cost + w, v))
        slowest = max(dist.values())
        return -1 if slowest == INF else slowest