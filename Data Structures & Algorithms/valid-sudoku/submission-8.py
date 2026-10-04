class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) != 9 or any(len(row) != 9 for row in board):
            return False
        
        row, col, box = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(9):
            for c in range(9):
                ch = board[r][c]

                if ch == '.':
                    continue

                b = (r // 3, c // 3)

                if ch in row[r] or ch in col[c] or ch in box[b]:
                    return False
                
                row[r].add(ch)
                col[c].add(ch)
                box[b].add(ch)
        return True