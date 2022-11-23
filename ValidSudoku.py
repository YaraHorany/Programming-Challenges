"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid(arr):
            seen = set()
            for val in arr:
                if val == '.':
                    continue
                if val in seen:
                    return False
                seen.add(val)
            return True
        
        #Row
        for row in board:
            if not valid(row):
                return False
        
        #column
        for j in range(9):
            col = [board[i][j] for i in range(9)]
            if not valid(col):
                return False
       
        #Block
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = [board[k][l] for k in range(i, i+3) for l in range(j, j+3)]
                if not valid(block):
                    return False
        return True