test_case1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
test_case2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                # Check row
                if board[i][j] != ".":
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])
                # Check column
                if board[j][i] != ".":
                    if board[j][i] in col_set:
                        return False
                    col_set.add(board[j][i])

        # Check subgrids
        for block_row in range(3):
            for block_col in range(3):
                subgrid_set = set()
                for i in range(3):
                    for j in range(3):
                        row = block_row * 3 + i
                        col = block_col * 3 + j
                        if board[row][col] != ".":
                            if board[row][col] in subgrid_set:
                                return False
                            subgrid_set.add(board[row][col])

        return True


sol = Solution()
print(sol.isValidSudoku(board=test_case2))


# class Solution(object):
#     def isValidSudoku(self, board):
#         res = []
#         for i in range(9):
#             for j in range(9):
#                 element = board[i][j]
#                 if element != ".":
#                     res += [(i, element), (element, j), (i // 3, j // 3, element)]
#         return len(res) == len(set(res))
