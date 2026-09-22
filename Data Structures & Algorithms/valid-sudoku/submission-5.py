class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_row = [set() for _ in range(9)]
        valid_col = [set() for _ in range(9)]
        valid_box = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                element = board[row][col]
                box = (row // 3) * 3 + (col // 3)
                if element != '.':
                    if (
                        (element in valid_row[row])
                        or (element in valid_col[col])
                        or (element in valid_box[box])
                    ):
                     return False
                valid_row[row].add(element)
                valid_col[col].add(element)
                valid_box[box].add(element)
        return True
