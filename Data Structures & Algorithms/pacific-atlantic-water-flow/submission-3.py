class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        def reach(start):
            path = set(start)
            q = deque(start)

            while q:
                r, c = q.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in path and heights[nr][nc] >= heights[r][c]):
                        path.add((nr, nc))
                        q.append((nr, nc))
            return path
        
        pacific = {(r, 0) for r in range(ROWS)} | {(0, c) for c in range(COLS)}
        atlantic = {(r, COLS -1) for r in range(ROWS)} | {(ROWS - 1, c) for c in range(COLS)}

        both = reach(pacific) & reach(atlantic)
        return [[r, c] for r, c in both]