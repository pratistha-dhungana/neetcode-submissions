class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = set()
        seen_col = set()
        seen_board = set()
        
        for row in range(9):
            for col in range(9):
                value = board[row][col]

                row_check = (row, value)
                col_check = (value, col)
                board_check = (row//3, col//3, value)

                if value == ".":
                    continue

                if row_check in seen_row:
                    return False
                else: 
                    seen_row.add(row_check)
                
                if col_check in seen_col:
                    return False
                else:
                    seen_col.add(col_check)

                if board_check in seen_board:
                    return False
                else:
                    seen_board.add(board_check)
        return True