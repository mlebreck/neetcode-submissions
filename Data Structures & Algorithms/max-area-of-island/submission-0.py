class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        best = 0 

        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c))
            area = 1

            while q:
                row, col = q.popleft()

                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1 and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        area += 1
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    best = max(best, bfs(r, c))
        return best