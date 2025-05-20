"""Valid Sudoku: Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/769/
"""

class Solution:

    def valid_board(self, board):
        """Time complexity: O(1) Space complexity: O(1)"""

        # Check rows
        for row in board:
            seen = set()
            for i in row:
                if i == '.':
                    continue
                if not i.isdigit() or not 1 <= int(i) <= 9 or i in seen:
                    return False
                seen.add(i)

        # Check columns
        for col in zip(*board):
            seen = set()
            for i in col:
                if i == '.':
                    continue
                if not i.isdigit() or not 1 <= int(i) <= 9 or i in seen:
                    return False
                seen.add(i)

        # Check 3x3 sub-boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        print(box_row, box_col, i, j, val)
                        if val == '.':
                            continue
                        if not val.isdigit() or not 1 <= int(val) <= 9 or val in seen:
                            return False
                        seen.add(val)

        return True

# Example usage:
# print(Solution().valid_board([["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]))

# print(Solution().valid_board([["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]))



