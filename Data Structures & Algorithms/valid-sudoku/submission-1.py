class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_seen = set()
        row_seen = set()
        sq_seen = set()
        for row in range(9):
            for col in range(9):

                value = board[row][col]

                row_check = (row, value)
                col_check = (value, col)
                sq_check = (row//3, col//3, value)
                
                if value == ".":
                    continue

                if row_check not in row_seen:
                    row_seen.add(row_check)
                else:
                    return False
                
                if col_check not in col_seen:
                    col_seen.add(col_check)
                else:
                    return False

                if sq_check not in sq_seen:
                    sq_seen.add(sq_check)
                else:
                    return False
        return True