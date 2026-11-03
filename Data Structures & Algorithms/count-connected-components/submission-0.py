class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        seen = set()
        count = 0

        def bfs(start):
            seen.add(start)
            q = deque([start])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
        
        for i in range(n):
            if i not in seen:
                bfs(i)
                count += 1
        return count