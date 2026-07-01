class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) != 9 or any(len(row) != 9 for row in board):
            return False

        seen = set()

        for r in range(9):
            for c in range(9):
                ch = board[r][c]

                if ch == '.':
                    continue

                if '1' > ch > '9':
                    return False

                box = (r // 3, c // 3)
                r_key = ('r', r, ch)
                c_key = ('c', c, ch)
                b_key = ('b', box[0], box[1], ch)

                if r_key in seen or c_key in seen or b_key in seen:
                    return False

                seen.add(r_key)
                seen.add(c_key)
                seen.add(b_key)

        return True




