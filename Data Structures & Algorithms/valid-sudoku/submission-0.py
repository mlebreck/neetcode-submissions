class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        if len(board) != 9 or any(len(row) != 9 for row in board):
            return False

        seen = set()

        for row in range(9):
            for col in range(9):
                ch = board[row][col]

                if ch == '.':
                    continue

                if ch < '1' or ch > '9':
                    return False

                box = (row // 3, col // 3)
                row_key = ('r', row, ch)
                col_key = ('c', col, ch)
                box_key = ('b', box[0], box[1], ch)

                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
        
        return True