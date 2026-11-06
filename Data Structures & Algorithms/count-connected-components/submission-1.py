class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        num = 0
        
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        seen = set()
        def bfs(start):
            seen.add(start)
            q = deque([start])

            while q:
                u = q.popleft()
                for v in adj[u]:
                    if v not in seen:
                        q.append(v)
                        seen.add(v)
        
        for i in range(n):
            if i not in seen:
                bfs(i)
                num += 1
        return num