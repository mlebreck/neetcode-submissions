class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) != 9 or any(len(row) != 9 for row in board):
            return False

        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(9):
            for c in range(9):
                ch = board[r][c]

                if ch == ".":
                    continue
                
                b = (r // 3, c // 3)
                
                if ch in rows[r] or ch in cols[c] or ch in boxes[b]:
                    return False
                
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[b].add(ch)

        return True