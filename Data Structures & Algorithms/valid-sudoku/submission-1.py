class Solution:
   def isValidSudoku(self, board: List[List[str]]) -> bool:
    row_mask = [0] * 9
    column_mask = [0] * 9
    square_mask = [0] * 9

    for row in range(9):
        for col in range(9):
            if board[row][col] == '.':
                continue
            bit = 1 << int(board[row][col]) - 1
            square_index = (row // 3) * 3 + (col // 3)

            if row_mask[row] & bit:
                return False
            if column_mask[col] & bit:
                return False
            if square_mask[square_index] & bit:
                return False
            
            row_mask[row] |= bit
            column_mask[col] |= bit
            square_mask[square_index] |= bit

    return True