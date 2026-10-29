class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        def reach(starts):
            seen = set(starts)
            q = deque(starts)

            while q:
                r, c = q.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in seen and heights[r][c] <= heights[nr][nc]):
                        seen.add((nr, nc))
                        q.append((nr, nc))
            return seen
        
        pacific = {(0, c) for c in range(COLS)} | {(r, 0) for r in range(ROWS)}
        atlantic = {(ROWS - 1, c) for c in range(COLS)} | {(r, COLS - 1) for r in range(ROWS)}

        both = reach(pacific) & reach(atlantic)
        return [[r, c] for r,c in both]

        
